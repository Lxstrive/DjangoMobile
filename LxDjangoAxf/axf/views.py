from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from .models import *
from .forms import LoginForm, RegisterForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login



# class CustomBackend(ModelBackend):
#     """
#         自定义登录类型
#         用户名和邮箱都可以登录
#     """
#
#     def authenticate(self, username=None, password=None, **kwargs):
#         try:
#             # 使用并级需要使用django.db.models 下的Q对象
#             user = UserProfile.objects.get(
#                 Q(username=username) | Q(email=username))
#             # 由于密码是密文传输，用户传进来的是明文 所以需要使用Django自带的user的
#             # check_password方法进行密码比对
#             if user.check_password():
#                 return user
#         except Exception as e:
#             return None

def home(request):
    # 主页
    banners = Wheel.objects.all()
    navs = Nav.objects.all()
    must_buys = Mustbuy.objects.all()
    shop_list = Shop.objects.all()
    mainshows = MainShow.objects.all()
    shop1 = shop_list[0]
    shop2 = shop_list[1:3]
    shop3 = shop_list[3:7]
    shop4 = shop_list[7:11]
    return render(request, 'home/home_.html', {
        'banners': banners,
        'navs': navs,
        'must_buys': must_buys,
        'shop1': shop1,
        'shop2': shop2,
        'shop3': shop3,
        'shop4': shop4,
        'mainshows': mainshows
    })


def market(request, categoryid, cid, sortid):
    # 闪送超市
    active = 'active'
    left_list = FoodType.objects.all()

    if cid == '0':
        goods_list = Goods.objects.filter(categoryid=categoryid)
    else:
        goods_list = Goods.objects.filter(categoryid=categoryid, childcid=cid)

    # 排序
    if sortid == '1':
        goods_list = goods_list.order_by('productnum')
    elif sortid == '2':
        goods_list = goods_list.order_by('-price')
    elif sortid == '3':
        goods_list = goods_list.order_by('price')

    group = left_list.get(typeid=categoryid)
    child_type_list = []
    child_names = group.childtypenames
    strs = child_names.split('#')
    for str in strs:
        str1 = str.split(':')
        obj = {'child_name': str1[0], 'child_id': str1[1]}
        child_type_list.append(obj)

    return render(request, 'market/market_.html', {
        'leftList': left_list,
        'active': active,
        'goods_list': goods_list,
        'child_type_list': child_type_list,
        'categoryid': categoryid,
        'cid': cid
    })


def cart(request):
    return render(request, 'cart/cart_.html')


def mine(request):
    return render(request, 'mine/mine_.html')


def user_login(request):
    # 登录功能
    if request.method == 'GET':
        return render(request, 'user/login.html')
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            try:
                user = authenticate(username=user_name, password=pass_word)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect(reverse('axf:mine'))
                else:
                    return render(request, 'user/login.html', {
                        'msg': '用户名或密码错误'
                    })
            except Exception as e:
                return HttpResponseRedirect(reverse('axf:login'))
    else:
        return HttpResponseRedirect(reverse('axf:login'))


def register(request):
    # 注册
    if request.method == 'GET':
        return render(request, 'user/user_register.html')
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('username', '')
            if UserProfile.objects.filter(name=user_name):
                return render(request, 'user/user_register.html', {
                    'msg': '用户名已存在'
                })
            user_email = request.POST.get('email', '')
            pass_word = request.POST.get('password', '')
            pass_word1 = request.POST.get('password1', '')
            if pass_word != pass_word1:
                return render(request, 'user/user_register.html', {})
            user_profile = UserProfile()
            user_profile.name = user_name
            user_profile.email = user_email
            user_profile.password = make_password(pass_word)
            user_profile.save()

            return HttpResponseRedirect(reverse('axf:login'))
    else:
        return render(request, 'user/user_register.html')
