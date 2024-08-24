from django.urls import path
from .views import DeedAPIView



urlpatterns = [
    path('api/v1/deedlist/', DeedAPIView.as_view()),
]