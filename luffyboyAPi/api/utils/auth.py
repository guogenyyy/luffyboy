# -*- coding: utf-8 -*-
# @File  : auth.py
# @Author: ggy
# @Date  : 2019/8/21
# @Software: PyCharm
import datetime

import pytz
from django.core.cache import cache
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from api.models import Token


class LoginAuth(BaseAuthentication):
    def authenticate(self, request):
        """
        1 对 token 设置 14 天有效时间
        2 缓存储存

        :param request:
        :return:
        """
        token = request.META.get("HTTP_AUTHORIZATION")

        # 1 校验是否存在 token 字符串
        # 1.1 缓存校验
        user = cache.get(token)
        if user:
            print("缓存校验成功！")
            return user, token

        token_obj = Token.objects.filter(key=token).first()
        # 数据库校验
        # 是否存在 token 字符串
        if not token_obj:
            raise AuthenticationFailed("认证失败！")

        # 2 校验是否在有效期内
        # print(token_obj.created)
        now = datetime.datetime.now()
        now = now.replace(tzinfo=pytz.timezone('UTC'))
        # print(now - token_obj.created)
        delta = now - token_obj.created
        # state = now - token_obj.created < datetime.timedelta(weeks=2)
        state = delta < datetime.timedelta(weeks=2)
        # print(state)

        if state:

            # 校验成功，写入缓存
            print("delta", delta)
            delta = datetime.timedelta(weeks=2) - delta
            print(delta.total_seconds())

            cache.set(token_obj.key, token_obj.user, min(delta.total_seconds(), 3600 * 24 * 7))
            print("数据库校验成功！")
            return token_obj.user, token_obj

        else:
            raise AuthenticationFailed("认证超时！")
