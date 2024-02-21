from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Recipe,Category


class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Recipe, RecipeAdmin)


class CategoryAdmin(MPTTModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Category, CategoryAdmin)