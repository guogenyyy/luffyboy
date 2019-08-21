# -*- coding: utf-8 -*-
# @File  : serializer.py
# @Author: ggy
# @Date  : 2019/8/21
# @Software: PyCharm
from rest_framework import serializers

from api.models import *


class CourseSerializers(serializers.ModelSerializer):
    """

    """
    class Meta:
        model = Course
        fields = "__all__"

    level = serializers.CharField(source="get_level_display")
    coursedetail_id = serializers.CharField(source="coursedetail.pk")


class CourseDetailSerializer(serializers.ModelSerializer):
    """

    """
    class Meta:
        model = CourseDetail
        fields = "__all__"

    name = serializers.CharField(source="course.name")
    prices = serializers.SerializerMethodField()
    brief = serializers.StringRelatedField(source='course.brief')
    study_all_time = serializers.StringRelatedField(source='hours')
    level = serializers.CharField(source='course.get_level_display')
    teachers_info = serializers.SerializerMethodField()
    # is_online = serializers.SerializerMethodField()
    recommend_coursesinfo =serializers.SerializerMethodField()

    def get_prices(self, instance):

        return [{
            'price': obj.price,
            'valid_period': obj.valid_period,
            'valid_period_text': obj.get_valid_period_display()
        } for obj in instance.course.price_policy.all()]

    def get_teachers_info(self, instance):
        return [{
            'name': obj.name,
            'image': obj.image
        } for obj in instance.teachers.all()]

    def get_recommend_coursesinfo(self, instance):
        return [{
            'name': obj.name,
            'course_image': obj.course_img
        } for obj in instance.recommend_courses.all()]
