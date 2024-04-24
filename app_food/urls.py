from rest_framework.routers import DefaultRouter

from app_food.views import CategoryViewSet, FoodViewSet

router = DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'food', FoodViewSet)

urlpatterns = router.urls

