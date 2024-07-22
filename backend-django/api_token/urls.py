from django.urls import path
from . import views

urlpatterns = [
    path('api_token', views.test_api_token, name='test-api-token'),
    path('api_mint_token', views.mint_token, name='mint-token'),
]