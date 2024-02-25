from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from . import models
from .models import Recipe,Category


@admin.register(models.UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'created', 'updated')
    search_fields = ['first_name', 'username', ]


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'content', 'steps', 'time', 'author')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Recipe, RecipeAdmin)


class CategoryAdmin(MPTTModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title', ]


admin.site.register(Category, CategoryAdmin)