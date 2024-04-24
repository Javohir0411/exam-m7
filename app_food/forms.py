from django.forms import ModelForm
from .models import Food, Category


class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = "__all__"


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
