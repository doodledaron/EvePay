from django.urls import path
from . import views

urlpatterns = [
    path('api_wallet', views.test_api_wallet_conn, name='test-api-token'),
    path('api_create_org_wallet', views.create_orgainsation_wallet, name='create-org-wallet'),
    path('api_create_user_wallet', views.create_user_wallet, name='create-user-wallet'),
    path('api_create_cat__wallet', views.create_wallet_category, name='create-wallet-category'),
    path('api_create_cat_entity', views.create_entity_category, name='create-entity-category'),
    path('api_create_entity', views.create_entity, name='create-entity'),

    # path('api_get_wallet', views.get_wallet, name='get-wallet'),
    # path('api_get_wallet_balance', views.get_wallet_balance, name='get-wallet-balance'),
]