from django.urls import path
from user import views


urlpatterns = [
    path('profile/', views.ProfileAPIView.as_view()),
    path('profile/<pk>/', views.ProfileUpdateAPIView.as_view()),
]
