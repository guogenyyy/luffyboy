from django.contrib import admin

# Register your models here.
from api.models import *

admin.site.site_header = '学成商城后台管理'
admin.site.index_title = '后台系统'
admin.site.site_title = '管理'


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'course_type', 'level', 'pub_date', 'period', 'order', 'status', ]
    list_filter = ['course_type', 'level', 'status']


@admin.register(CourseDetail)
class CourseDetailAdmin(admin.ModelAdmin):
    list_display = ['course', 'hours', 'course_slogan', 'video_brief_link']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'title']
    list_filter = []


@admin.register(PricePolicy)
class PricePolicyAdmin(admin.ModelAdmin):
    list_display = ['object_id']


@admin.register(CourseChapter)
class CourseChapterAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_create', 'pub_date']


@admin.register(CourseSection)
class CourseSectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'video_time']


@admin.register(OftenAskedQuestion)
class OftenAskedQuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer']


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['name', 'brief', 'coupon_type', 'quantity']


@admin.register(CouponRecord)
class CouponRecordAdmin(admin.ModelAdmin):
    list_display = ['status', 'get_time', 'used_time']
    list_filter = ['status']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['payment_type', 'payment_number', 'order_number', 'status', 'order_type', 'date', 'pay_time',
                    'cancel_time']


@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['object_id', 'content', 'valid_period_display']


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'mobile', 'qq', 'weixin', 'gender', 'id_card', 'is_active', 'is_staff', 'name',
                    'role', 'date_joined']
    list_filter = ['gender', 'role']
