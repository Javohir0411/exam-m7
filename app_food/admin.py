from django.contrib import admin
from .models import Food, Category


class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'food_name', 'food_recipe', 'food_price')
    search_fields = ('food_name',)
    ordering = ['food_name']


admin.site.register(Food, FoodAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'cat_name')
    search_fields = ('cat_name',)
    ordering = ['cat_name']


admin.site.register(Category, CategoryAdmin)
