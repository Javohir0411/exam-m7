import django_filters
from django.db.models import Q
from django_filters import FilterSet, CharFilter

from app_food.models import Category, Food


class FoodFilter(FilterSet):
    keyword = CharFilter(method='my_filter', label='Search keyword')

    class Meta:
        model = Food
        fields = {

        }

    def my_filter(self, queryset, value):
        try:
            return queryset.filter(Q(book_year=value))
        except:
            return queryset.filter(
                Q(food_name__icontains=value) |
                Q(food_category__category_name__icontains=value)
            )
