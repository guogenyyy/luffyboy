from django.contrib import admin

# Register your models here.
from api.models import *


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(CourseDetail)
class CourseDetailAdmin(admin.ModelAdmin):
    pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass


@admin.register(PricePolicy)
class PricePolicyAdmin(admin.ModelAdmin):
    pass


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    pass


@admin.register(CouponRecord)
class CouponRecordAdmin(admin.ModelAdmin):
    pass

