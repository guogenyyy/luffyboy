# -*- coding: utf-8 -*-
# @File  : urls.py
# @Author: ggy
# @Date  : 2019/8/31
# @Software: PyCharm

from django.urls import path, re_path

from api.views.account import AccountView
from api.views.captcha import CaptchaView
from api.views.course import CourseView, CourseDetailView
from api.views.login import LoginView
from api.views.payment import PaymentView
from api.views.shoppingcart import ShoppingCartView

urlpatterns = [
    path('courses/', CourseView.as_view({"get": "list"})),
    re_path('courses/detail/$', CourseDetailView.as_view({'get': 'list'})),
    re_path('courses/detail/(?P<pk>\d+)/', CourseDetailView.as_view({'get': 'retrieve'})),

    # 登录
    path('login/', LoginView.as_view()),

    # 购物车
    path('shoppingcart/', ShoppingCartView.as_view()),
    path('account/', AccountView.as_view()),
    path('payment/', PaymentView.as_view()),

    # 极验验证
    path('captcha_check/', CaptchaView.as_view()),

]


