from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse

# from recipe_site.cookapp.views import upload_image


class Recipe(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название рецепта')
    slug = models.SlugField(max_length=150)
    category = TreeForeignKey('Category', on_delete=models.PROTECT, related_name='posts', verbose_name='Категория')
    content = models.TextField(max_length=1500,verbose_name='Описание')
    steps = models.TextField(max_length=15000, verbose_name='Шаги приготовления')
    time = models.TextField(max_length=150, verbose_name='Время приготовления')
   # image = models.ImageField(upload_to=upload_image)
    author = models.TextField(max_length=150, verbose_name='Автор')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class Category(MPTTModel):
    title = models.CharField(max_length=50, unique=True, verbose_name='Название категории')
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name='Родительская категория')
    slug = models.SlugField(max_length=50)

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('post-by-category', args=[str(self.slug)])

    def __str__(self):
        return self.title
