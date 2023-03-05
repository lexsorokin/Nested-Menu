from django.shortcuts import render
from app_content.models import Goods
from app_menu.models import Category


def get_category_goods(request, slug):
    category = Category.objects.get(slug=slug)
    category_goods = Goods.objects.filter(category=category)
    return render(
        request=request,
        template_name='goods/goods_list.html',
        context={
            'category': category,
            'category_goods': category_goods,
        }
    )
