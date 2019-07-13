from django.contrib import admin
from .models import *


class ArticleAdmin(admin.ModelAdmin):
    pass


class PofileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Article, ArticleAdmin)
admin.site.register(Profile, PofileAdmin)
