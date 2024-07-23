import requests
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view

# Token API_KEY and API_PASSWORD
API_KEY = 'd2e5b49b8d126cd2687d9c61b8f6ba2e64e856d6c34cdf27fb3cb9b59bd2d2a3'
API_PASSWORD = 'sk_43375ea6665657b0030e702f30144c664239d43c03f0c9b733afd41d47db02aa'
BASE_API_URL = 'https://service-testnet.maschain.com'

headers = {
    'client_id': f'{API_KEY}',
    'client_secret': f'{API_PASSWORD}',
    'content-type': 'application/json'
}

def test_api_token_conn(request):
    response = requests.get(BASE_API_URL, headers=headers)
    if response.status_code == 200:
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': response.text}, status=response.status_code)

# Temporarily allow GET requests for testing

