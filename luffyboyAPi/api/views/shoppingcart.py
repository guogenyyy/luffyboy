# -*- coding: utf-8 -*-
# @File  : shoppingcart.py
# @Author: ggy
# @Date  : 2019/8/21
# @Software: PyCharm
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Course, PricePolicy
from api.utils.response import BaseResponse
from api.utils.exceptions import CommonException
from api.utils.auth import LoginAuth

import json
import redis

cache = redis.Redis(decode_responses=True)


class ShoppingCartView(APIView):
    authentication_classes = [LoginAuth]

    def post(self, request):
        """
        模拟请求数据：
        {
            "course_id": 1,
            "price_policy_id": 2
        }
        :param request:
        :return:
        """

        # 1 获取请求数据
        course_id = request.data.get("course_id")
        price_policy_id = request.data.get("price_policy_id")
        user_id = request.user.pk

        res = BaseResponse()

        # 2.校验数据
        try:
            # 2.1 校验课程是否存在
            course_obj = Course.objects.get(pk=course_id)
            # 2.2 校验价格策略是否合法
            # ret = course_obj.price_policy.all()
            # print(ret)
            price_policy_dict = {}
            for price_policy in course_obj.price_policy.all():
                price_policy_dict[price_policy.pk] = {
                    "valid_period": price_policy.valid_period,
                    "valid_period_text": price_policy.get_valid_period_display(),
                    "price": price_policy.price,
                    "default": price_policy_id == price_policy.pk
                }

            if price_policy_id not in price_policy_dict:
                raise CommonException(1002, "价格策略错误！")
            pp = PricePolicy.objects.get(pk=price_policy_id)

            # 3 写入 redis

            shoppingcar_key = settings.SHOPPINGCAR_KEY % (user_id, course_id)
            shoppingcar_val = {
                "title": course_obj.name,
                "img": course_obj.course_img,
                "relate_price_policy": price_policy_dict,
                "choose_price_policy_id": price_policy_id,
                "price": pp.price,
                "valid_period": pp.valid_period,
                "valid_period_text": pp.get_valid_period_display(),
            }

            cache.set(shoppingcar_key, json.dumps(shoppingcar_val))
            res.data = "加入购物车成功！"

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
