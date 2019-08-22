# -*- coding: utf-8 -*-
# @File  : payment.py
# @Author: ggy
# @Date  : 2019/8/22
# @Software: PyCharm
import time
import json
import datetime
import uuid

from django.core.exceptions import ObjectDoesNotExist

from rest_framework.views import APIView
from rest_framework.response import Response

from api.utils.auth import LoginAuth
from api.utils.response import BaseResponse
from api.utils.exceptions import CommonException
from api.utils.pay import AliPay
from api.models import *


class PaymentView(APIView):
    authentication_classes = [LoginAuth]

    def get_alipay(self):

        # 沙箱环境地址：https://openhome.alipay.com/platform/appDaily.htm?tab=info
        app_id = "2016091100486897"
        # POST请求，用于最后的检测
        notify_url = "http://47.94.172.250:8804/page2/"
        # notify_url = "http://www.wupeiqi.com:8804/page2/"
        # GET请求，用于页面的跳转展示
        return_url = "http://47.94.172.250:8804/page2/"
        # return_url = "http://www.wupeiqi.com:8804/page2/"
        merchant_private_key_path = "keys/app_private_2048.txt"
        alipay_public_key_path = "keys/alipay_public_2048.txt"

        alipay = AliPay(
            appid=app_id,
            app_notify_url=notify_url,
            return_url=return_url,
            app_private_key_path=merchant_private_key_path,
            alipay_public_key_path=alipay_public_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥
            debug=True,  # 默认False,
        )
        return alipay

    def cal_coupon_price(self, price, coupon_record_obj):
        """

        :param price:
        :param coupon_record_obj:
        :return:
        """
        coupon_type = coupon_record_obj.coupon.content_type
        money_equivalent_value = coupon_record_obj.coupon.money_equivalent_value
        off_percent = coupon_record_obj.coupon.off_percent
        minimum_consume = coupon_record_obj.coupon.minimum_consume

        rebate_price = 0

        if coupon_type == 0:  # 立减卷
            rebate_price = price - money_equivalent_value
            if rebate_price <= 0:
                rebate_price = 0
        elif coupon_type == 1:  # 满减卷
            if minimum_consume > price:
                raise CommonException(1007, "优惠卷未达到最低消费水平")
            else:
                rebate_price = price - money_equivalent_value
        elif coupon_type == 2:
            rebate_price = price * off_percent / 100

        return rebate_price

    def post(self, request):
        """
        模拟前端数据：
            {
                is_bei: true,
                course_list = [
                    {
                        course_id: 1,
                        default_price_policy_id: 1,
                        coupon_record_id: 2
                    },
                    {
                        course_id: 2,
                        default_price_policy_id: 4,
                        coupon_record_id: 6
                    }
                ],
                global_coupon_id: 3,
                pay_money: 298
            }

        :param request:
        :return:
        """

        # 1. 获取数据
        is_bei = request.data.get("is_beili")
        course_list = request.data.get("course_list")
        global_coupon_id = request.data.get("global_coupon_id")
        pay_money = request.data.get("pay_money")
        user_id = request.user.pk

        res = BaseResponse()

        # 2. 校验数据
        # 2.1 校验每一个课程
        try:
            price_list = []
            for course in course_list:
                course_id = course.gat("course_id")
                default_price_policy_id = course.gat("default_price_policy_id")
                coupon_record_id = course.gat("coupon_record_id")

                # 2.1.1 校验课程是否存在
                course_obj = Course.objects.get(pk=course_id)

                # 2.1.2 校验价格策略
                if default_price_policy_id not in [obj.pk for obj in course_obj.price_policy.all()]:
                    raise CommonException(1002, "价格策略错误！")

                pp = PricePolicy.objects.get(pk=default_price_policy_id)
                if coupon_record_id:
                    # 2.1.3 校验课程优惠卷

                    now = datetime.datetime.now()
                    coupon_record_obj = CouponRecord.objects.filter(
                        pk=coupon_record_id,
                        account=request.user,
                        coupon__content_type=9,
                        coupon__object_id=course_id,
                        status=0,
                        coupon__valid_begin_date__lte=now,
                        coupon__valid_end_date__gte=now

                    ).first()

                    if not coupon_record_obj:
                        raise CommonException(1003, "课程优惠卷异常！")

                    # 计算折后价格
                    rebate_money = self.cal_coupon_price(pp.price, coupon_record_obj)
                    price_list.append(rebate_money)
                else:
                    price_list.append(pp.price)

            final_price = sum(price_list)

            # 2.2校验通用优惠卷
            if global_coupon_id:
                # 2.2.1 校验通用优惠卷合法
                now = datetime.datetime.now()
                g_coupon_record_obj = CouponRecord.objects.filter(
                    pk=global_coupon_id,
                    account=request.user,
                    coupon__content_type=9,
                    coupon__object_id=None,
                    status=0,
                    coupon__valid_begin_date__lte=now,
                    coupon__valid_end_date__gte=now
                ).first()
                if not g_coupon_record_obj:
                    raise CommonException(1004, "通用优惠卷异常！")

                # 2.2.2 计算折后价格
                final_price = self.cal_coupon_price(final_price, g_coupon_record_obj)

            # 2.3校验贝里
            if json.loads(is_bei):
                final_price = final_price - request.user.beili / 10

                if final_price < 0:
                    final_price = 0

            # 2.4 校验最终价格
            if final_price != pay_money:
                raise CommonException(1005, "支付价格异常！")

            # 3.生成订单
                # 生成订单表

            order_obj = Order.objects.create(
                payment_type=1,
                order_number=uuid.uuid4(),
                account=request.user,
                status=1,
                order_type=1,
                actual_amount=pay_money
            )
            print("course_list", course_list)

            for course_item in course_list:
                OrderDetail.objects.create(
                    order=order_obj,
                    content_type_id=14,
                    object_id=course_item.get("course_id"),
                    original_price=course_item.get("original_price"),
                    price=course_item.get("valid_period"),
                    valid_period=course_item.get("valid_period"),
                    valid_period_display=course_item.get("valid_period_display")
                )

            # 4. 调用 alipay 接口
            alipay = self.get_alipay()
            # 生成支付的url
            query_params = alipay.direct_pay(
                subject="路飞学城",  # 商品简单描述
                out_trade_no="x345" + str(time.time()),  # 商户订单号
                total_amount=pay_money,  # 交易金额(单位: 元 保留俩位小数)
            )

            pay_url = "https://openapi.alipaydev.com/gateway.do?{}".format(query_params)
            res.data = {
                "url": pay_url
            }

        except ObjectDoesNotExist as e:
            res.code = 1001
            res.msg = "课程不存在！"

        except CommonException as e:
            res.code = e.code
            res.msg = e.msg

        return Response(res.dict)
