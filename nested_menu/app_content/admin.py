from django.contrib import admin
from .models import Goods


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'slug', 'creation_date',]
    prepopulated_fields = {"slug": ("name",)}



