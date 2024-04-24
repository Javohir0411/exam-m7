# from django.shortcuts import render
# from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
#
# from app_food.models import Category, Food

#
# # FUNCTION BASED VIEWS
#
# def index(request):
#     return render(request, 'interface/index.html')
#
#
# def recipe(request):
#     foods = Food.objects.all()
#     return render(request, 'interface/recipe.html', {"foods": foods})
#
#
# def contact(request):
#     return render(request, 'interface/contact.html')
#
#
# # CLASS BASED VIEWS
#
# class AddCategoryView(CreateView):
#     template_name = 'categories/add_category.html'
#     model = Category
#
#
# class DeleteCategoryView(DeleteView):
#     template_name = 'categories/delete_category.html'
#     model = Category
#
#
# class AddFoodView(CreateView):
#     template_name = 'foods/add_food.html'
#     model = Food
#
#
# class UpdateFoodView(UpdateView):
#     template_name = 'foods/edit_food.html'
#     model = Food
#
#
# class ListFoodView(DetailView):
#     template_name = 'interface/menu.html'
#     model = Food
#
#
#
# class DeleteFoodView(DeleteView):
#     template_name = 'foods/delete_food.html'
#     model = Food

from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from rest_framework import viewsets

from .models import Food, Category
from .forms import FoodForm, CategoryForm

from app_food.permissions import MyPermissions
from app_food.serializers import (
    CategorySerializer,
    FoodSerializer,
    FoodDetailSerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [MyPermissions]


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    permission_classes = [MyPermissions]

    def get_serializer_class(self):
        if self.action == 'list':
            return FoodSerializer
        else:
            return FoodDetailSerializer
