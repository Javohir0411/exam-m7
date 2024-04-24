from django.urls import path
from .views import (
    RegisterView,
    insert_email_4_change_password,
    reset_password,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='signup'),
    path('password_reset/email/', insert_email_4_change_password, name='password_reset'),
    path('reset_password/', reset_password, name='reset_password'),
]
