from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from . import models
from .models import Recipe,Category


@admin.register(models.UserModel)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ('chat_id', 'first_name', 'last_name', 'username', 'created', 'updated')
    search_fields = ['chat_id', 'first_name', 'username', ]
class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Recipe, RecipeAdmin)


class CategoryAdmin(MPTTModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)