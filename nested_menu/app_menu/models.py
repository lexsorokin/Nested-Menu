from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(
        verbose_name='Наименование',
        max_length=50,
        unique=True,
    )
    parent = TreeForeignKey(
        'self',
        verbose_name='Категория',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='parent_to_child',
    )
    slug = models.SlugField(
        max_length=150,
        null=True,
    )

    class MPTTMeta:
        order_insertion_by = ['name',]

    class Meta:
        unique_together = [['parent', 'slug',]]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('good_by_category', args=[str(self.slug)])

    def __str__(self):
        return f'{self.name}, {self.parent}'
