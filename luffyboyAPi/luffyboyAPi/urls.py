"""luffyboyAPi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from api.views.course import CourseView, CourseDetailView
from api.views.login import LoginView
from api.views.shoppingcart import ShoppingCartView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', CourseView.as_view({"get": "list"})),
    re_path('courses/detail/$', CourseDetailView.as_view({'get': 'list'})),
    re_path('courses/detail/(?P<pk>\d+)/', CourseDetailView.as_view({'get': 'retrieve'})),

    # 登录
    path('login/', LoginView.as_view()),

    # 购物车
    path('shoppingcart/', ShoppingCartView.as_view()),
]
