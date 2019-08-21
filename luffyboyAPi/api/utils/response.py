# -*- coding: utf-8 -*-
# @File  : response.py
# @Author: ggy
# @Date  : 2019/8/21
# @Software: PyCharm


class BaseResponse(object):
    def __init__(self):
        self.code = 1000
        self.data = None
        self.msg = ""

    @property
    def dict(self):

        return self.__dict__


if __name__ == '__main__':

    res = BaseResponse()

    print(res.dict)

