from django.urls import path
from . import views

urlpatterns = [
    path('api/test/', views.api_test, name='api_test'),
]

