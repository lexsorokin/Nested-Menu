from django.urls import path
from app_menu.views import CategoryListView

urlpatterns = [
    path('', CategoryListView.as_view(), name='category_list'),
]