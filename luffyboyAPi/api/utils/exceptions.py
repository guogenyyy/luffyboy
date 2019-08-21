# -*- coding: utf-8 -*-
# @File  : exceptions.py
# @Author: ggy
# @Date  : 2019/8/21
# @Software: PyCharm


class CommonException(Exception):
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg
