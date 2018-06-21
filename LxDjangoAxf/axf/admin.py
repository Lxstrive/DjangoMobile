from django.contrib import admin

from .models import *


class ShopAdmin(admin.ModelAdmin):
    pass


class MainShowAdmin(admin.ModelAdmin):
    pass


class MustbuyAdmin(admin.ModelAdmin):
    pass


class NavAdmin(admin.ModelAdmin):
    pass


class WheelAdmin(admin.ModelAdmin):
    pass


admin.site.register(Shop, ShopAdmin)
admin.site.register(MainShow, MainShowAdmin)
admin.site.register(Mustbuy, MustbuyAdmin)
admin.site.register(Nav, NavAdmin)
admin.site.register(Wheel, WheelAdmin)
