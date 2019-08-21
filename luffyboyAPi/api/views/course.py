# -*- coding: utf-8 -*-
# @File  : course.py
# @Author: ggy
# @Date  : 2019/8/21
# @Software: PyCharm
from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from api.models import *
from api.utils.serializer import CourseSerializers, CourseDetailSerializer
from api.utils.auth import LoginAuth


class CourseView(ModelViewSet):
    """

    """
    authentication_classes = [LoginAuth]
    queryset = Course.objects.all()
    serializer_class = CourseSerializers


class CourseDetailView(ModelViewSet):
    """

    """
    authentication_classes = [LoginAuth]
    queryset = CourseDetail.objects.all()
    serializer_class = CourseDetailSerializer
