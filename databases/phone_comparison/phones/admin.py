from django.contrib import admin
from .models import Phone, Apple, Asus, Samsung, Xiaomi


# Register your models here.
@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    pass


@admin.register(Apple)
class AppleAdmin(admin.ModelAdmin):
    pass


@admin.register(Samsung)
class SamsungAdmin(admin.ModelAdmin):
    pass


@admin.register(Asus)
class AsusAdmin(admin.ModelAdmin):
    pass


@admin.register(Xiaomi)
class XiaomiAdmin(admin.ModelAdmin):
    pass
