from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

# JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from uzbek_cuisine import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Uzbek cuisine Backend",
        default_version='v1',
        description="Backend for uzbek cuisine project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="javohirabduhakimov979@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/food/', include('app_food.urls')),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    # JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
