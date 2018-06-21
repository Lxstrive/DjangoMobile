# coding: utf-8

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """
        用户表设计
        如果Django自带的用户表无法满足的时候继承原表增加自己的字段
    """

    gender = models.CharField(choices=(('male', u'男'), ('female', u'女')),
                              default='female', max_length=6)
    image = models.ImageField(upload_to='image/%Y/%m',
                              default=u'image/default.png', max_length=100)

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Wheel(models.Model):
    """
        轮播商品信息
    """
    name = models.CharField(max_length=20, verbose_name='u商品名称')
    img = models.ImageField(upload_to='img/%Y/%m', verbose_name=u'轮播图',
                            max_length=100)
    trackid = models.CharField(max_length=20, verbose_name=u'跳转ID')

    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Nav(models.Model):
    """
        导航条模型
    """
    name = models.CharField(max_length=20, verbose_name='导航名称')
    img = models.ImageField(upload_to='img/%Y/%m', verbose_name='导航图片',
                            max_length=100)
    trackid = models.CharField(max_length=20, verbose_name='跳转ID')

    class Meta:
        verbose_name = '导航条'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Mustbuy(models.Model):
    """
        每日必购
    """
    name = models.CharField(max_length=20, verbose_name='每日必购')
    img = models.ImageField(upload_to='img/%Y/%m', verbose_name='必购图片',
                            max_length=100)
    trackid = models.CharField(max_length=20, verbose_name='跳转ID')

    class Meta:
        verbose_name = '每日必购'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Shop(models.Model):
    """
        便利店模型
    """
    name = models.CharField(max_length=20, verbose_name='便利店')
    img = models.ImageField(upload_to='img/%Y/%m', verbose_name='便利店图片',
                            max_length=100)
    trackid = models.CharField(max_length=20, verbose_name='跳转ID')

    class Meta:
        verbose_name = '便利店'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class MainShow(models.Model):
    """
        主要显示
    """
    name = models.CharField(max_length=20, verbose_name='便利店')
    img = models.ImageField(upload_to='img/%Y/%m', verbose_name='便利店图片',
                            max_length=100)
    trackid = models.CharField(max_length=20, verbose_name='跳转ID')
    # 定义一些需要的数据字段
    categoryid = models.CharField(max_length=16)
    brandname = models.CharField(max_length=100)

    # 第一件商品
    img1 = models.CharField(max_length=200)
    childcid1 = models.CharField(max_length=16)
    productid1 = models.CharField(max_length=16)
    longname1 = models.CharField(max_length=100)

    # 价格默认0,促销价默认1
    price1 = models.FloatField(default=0)
    marketprice1 = models.FloatField(default=1)

    # 第二件商品
    img2 = models.CharField(max_length=200)
    childcid2 = models.CharField(max_length=16)
    productid2 = models.CharField(max_length=16)
    longname2 = models.CharField(max_length=100)
    price2 = models.FloatField(default=0)
    marketprice2 = models.FloatField(default=1)

    # 第三件商品
    img3 = models.CharField(max_length=200)
    childcid3 = models.CharField(max_length=16)
    productid3 = models.CharField(max_length=16)
    longname3 = models.CharField(max_length=100)
    price3 = models.FloatField(default=0)
    marketprice3 = models.FloatField(default=1)

    class Meta:
        # 定义表名
        db_table = "axf_mainshow"
        verbose_name = '主要商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class FoodType(models.Model):
    """
        商品分类模型
    """

    typeid = models.CharField(max_length=16, verbose_name='分类ID')
    typename = models.CharField(max_length=100, verbose_name='分类名称')
    childtypenames = models.CharField(max_length=200, verbose_name='子类名称')
    typesort = models.IntegerField(default=1, verbose_name='排序')

    class Meta:
        verbose_name = '商品分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.typename


class Goods(models.Model):
    """
       商品模型
    """
    productid = models.CharField(max_length=16)
    productimg = models.CharField(max_length=200)
    productname = models.CharField(max_length=100)
    productlongname = models.CharField(max_length=200)
    isxf = models.IntegerField(default=1)
    pmdesc = models.CharField(max_length=100)
    specifics = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    marketprice = models.FloatField(default=1)
    categoryid = models.CharField(max_length=16)
    childcid = models.CharField(max_length=16)
    childcidname = models.CharField(max_length=100)
    dealerid = models.CharField(max_length=16)
    storenums = models.IntegerField(default=1)
    productnum = models.IntegerField(default=1)

    class Meta:
        verbose_name = '食物信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.productname


