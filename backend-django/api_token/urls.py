from django.urls import path
from . import views

urlpatterns = [
    path('api_token', views.test_api_token_conn, name='test-api-token'),
    path('api_mint_token', views.mint_token, name='mint-token'),
    path('api_pause_token', views.pause_token, name='pause-token'),
    path('api_resume_token', views.resume_token, name='resume-token'),
    path('api_burn_token', views.burn_token, name='burn-token'),
    path('api_transfer_token/<int:capacity_used>', views.transfer_token, name='transfer-token'),
    path('api_transfer_owner', views.transfer_owner, name='transfer-owner'),
    path('api_check_balance', views.check_balance, name='check-balance'),
    path('callback-handler', views.callback_handler, name='callback_handler'),
    path('api_get_transaction_to/<str:wallet_address>', views.get_transaction_filter_to, name='get-transaction-to'),
    path('api_get_transaction_from/<str:wallet_address>', views.get_transaction_filter_from, name='get-transaction-from'),
]