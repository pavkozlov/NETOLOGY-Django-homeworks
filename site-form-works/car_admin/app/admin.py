from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    search_fields = ['brand', 'model']
    list_display = ['brand', 'model', 'review_count']
    list_filter = ['brand']
    ordering = ('-id',)


class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm
    search_fields = ['title']
    list_display = ['car', 'title']
    ordering = ('-id',)


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
