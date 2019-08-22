# -*- coding: utf-8 -*-
# @File  : middleware.py
# @Author: ggy
# @Date  : 2019/8/22
# @Software: PyCharm

from django.utils.deprecation import MiddlewareMixin


class CorsMiddleware(MiddlewareMixin):

    def process_response(self, request, response):

        if request.method == "OPTIONS":
            response["Access-Control-Allow-Headers"] = ["Content-Type"]

        # 解决跨域访问， 可以修改为指定域名地址访问
        response["Access-Control-Allow-Origin"] = "*"

        return response

