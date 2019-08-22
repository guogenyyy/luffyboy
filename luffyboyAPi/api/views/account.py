# -*- coding: utf-8 -*-
# @File  : shoppingcart.py
# @Author: ggy
# @Date  : 2019/8/21
# @Software: PyCharm
import datetime
import json
import redis

from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Course, CouponRecord
from api.utils.response import BaseResponse
from api.utils.exceptions import CommonException
from api.utils.auth import LoginAuth


cache = redis.Redis(decode_responses=True)


class AccountView(APIView):
    authentication_classes = [LoginAuth]

    def get_coupon_dict(self, request, course_id=None):
        """

        :param request:
        :param course_id:
        :return:
        """

        now = datetime.datetime.now()
        coupon_record_list = CouponRecord.objects.filter(
            account=request.user,
            coupon__content_type=9,
            coupon__object_id=course_id,
            status=0,
            coupon__valid_begin_date__lte=now,
            coupon__valid_end_date__gte=now
        )
        print("coupon_record_list", coupon_record_list)
        coupons = {}
        for coupon_record in coupon_record_list:
            coupons[coupon_record.pk] = {
                "name": coupon_record.coupon.name,
                "content_type": coupon_record.coupon.content_type,
                "money_equivalent_value": coupon_record.coupon.money_equivalent_value,
                "off_percent": coupon_record.coupon.off_percent,
                "minimum_consume": coupon_record.coupon.minimum_consume,

            }
        return coupons

    def post(self, request):
        """
        模拟请求数据：
        {
            "course_id_list":[1, 2]
        }
        :param request:
        :return:
        """

        # 1 获取请求数据
        course_id_list = request.data.get("course_id_list")
        user_id = request.user.pk
        res = BaseResponse()

        # 2.校验数据
        try:
            # 2.1 校验课程是否存在
            for course_id in course_id_list:  # 结算情况： 1. 直接购买 2.购物车购买

                # 结算 key
                account_key = settings.ACCOUNT_KEY % (user_id, course_id)
                # 结算字典
                account_val = {}

                # 获取课程基本信息
                shoppingcar_key = settings.SHOPPINGCAR_KEY % (user_id, course_id)
                course_obj = Course.objects.get(pk=course_id)
                course_info = json.loads(cache.get(shoppingcar_key))

                # 添加到结算字典中
                account_val["course_info"] = course_info

                # 获取优惠卷信息：查询当前用户的当前课程的有效的未使用的优惠卷
                coupons = self.get_coupon_dict(request, course_id)
                # 将优惠卷字典添加到结算字典中
                account_val["coupons"] = coupons
                print("account_val", type(account_val))

                cache.set(account_key, json.dumps(account_val))

            # 获取通用优惠卷
            global_coupons = self.get_coupon_dict(request)
            cache.set("global_coupons_%s" % user_id, json.dumps(global_coupons))

        except CommonException as e:
            res.code = e.code
            res.msg = "课程不存在"

        except ObjectDoesNotExist as e:
            res.code = 1001
            res.msg = "课程不存在"

        return Response(res.dict)

    def get(self, request):
        """

        :param request:
        :return:
        """
        pass
