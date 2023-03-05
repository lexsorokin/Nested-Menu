from django.urls import path
from app_content.views import get_category_goods

urlpatterns = [
    path('<str:slug>/', get_category_goods, name='good_by_category')
]