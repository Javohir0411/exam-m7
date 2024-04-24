# !!!!!!! API YARATISH UCHUN TAYYORLAB QO'YILDI !!!!!!!!

from rest_framework import serializers
from .models import Food, Category


class FoodSerializer(serializers.ModelSerializer):
    food_detail_url = serializers.SerializerMethodField(read_only=True, source='get_food_detail_url')

    class Meta:
        model = Food
        # fields = ['id', 'food_name', 'food_price', 'food_detail_url']
        fields = "__all__"
        depth = 1

    def get_food_detail_url(self, obj):
        return f"http://localhost:8000/api/v1/food/{obj.id}"


class FoodDetailSerializer(serializers.ModelSerializer):
    food_category_info = serializers.SerializerMethodField(read_only=True, source='get_food_category_info')

    class Meta:
        model = Food
        fields = "__all__"
        # depth = 1

    def get_food_category_info(self, obj):
        info = {
            'category_id': obj.food_category.id,
            'category_name': obj.food_category.cat_name
        }
        return info

    def edit_food_url(self, obj):
        return f"http://localhost:8000/api/v1/food/edit/{obj.id}"


class FoodEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"


class FoodDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



