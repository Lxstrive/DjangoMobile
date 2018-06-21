# !/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = '_X.xx_'
__date__ = '2018/6/19 12:35'

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=20)
    password = forms.CharField(required=True, min_length=6)


class RegisterForm(forms.Form):
    # 对email进行验证
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=6)
