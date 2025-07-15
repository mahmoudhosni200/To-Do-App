from django.urls import path # type: ignore
from .views import *
from rest_framework.routers import DefaultRouter # type: ignore



urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
]