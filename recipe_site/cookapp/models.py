from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse


class Recipe(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название рецепта')
    slug = models.SlugField(max_length=150)
    category = TreeForeignKey('Category', on_delete=models.PROTECT, related_name='posts', verbose_name='Категория')
    content = models.TextField(max_length=1500, verbose_name='Описание')
    steps = models.TextField(max_length=15000, verbose_name='Шаги приготовления')
    time = models.TextField(max_length=150, verbose_name='Время приготовления')
    # file = models.FileField(upload_to='pecipe_img/')
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


class UserModel(models.Model):
    chat_id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50,blank=True, null=True,verbose_name='Фамилия')
    username = models.CharField(max_length=50,blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Зарегистрирован')
    updated = models.DateTimeField(auto_now=True, verbose_name='Последняя активность')

    objects = models.Manager()

    class Meta:
        ordering = ['-updated']
        verbose_name = 'Пользователь сайта'
        verbose_name_plural = 'Пользователи сайта'

    def __str__(self):
        return self.first_name