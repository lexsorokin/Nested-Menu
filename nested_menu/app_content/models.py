from django.db import models
from mptt.fields import TreeForeignKey


class Goods(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=100,
        null=True,
    )
    description = models.TextField(
        verbose_name='Содержание',
        null=True,
    )
    category = TreeForeignKey(
        'app_menu.Category',
        verbose_name='Категория',
        on_delete=models.PROTECT,
        related_name='goods_to_category',
    )
    slug = models.SlugField(
        max_length=150,
    )
    creation_date = models.DateField(
        verbose_name='Дата создания',
        null=True,
        auto_now_add=True,
    )
    update_date = models.DateField(
        verbose_name='Дата обновления',
        null=True,
        auto_now=True,
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name}, {self.category}'
