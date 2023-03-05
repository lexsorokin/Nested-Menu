from django.shortcuts import render
from django.views.generic import ListView
from app_menu.models import Category


class CategoryListView(ListView):
    model = Category
    template_name = "menu/category_list.html"
    context_object_name = 'categories'
