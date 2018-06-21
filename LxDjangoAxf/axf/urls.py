# !/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = '_X.xx_'
__date__ = '2018/6/17 21:23'


from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^market/(\d+)/(\d+)/(\d+)/$', views.market, name='market'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^mine/$', views.mine, name='mine'),
    # 登录
    url(r'^login/$', views.user_login, name='login'),
    # 注册
    url(r'^register/$', views.register, name='register')

]