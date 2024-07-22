import requests
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import api_view


API_KEY = 'd2e5b49b8d126cd2687d9c61b8f6ba2e64e856d6c34cdf27fb3cb9b59bd2d2a3'
API_PASSWORD = 'sk_43375ea6665657b0030e702f30144c664239d43c03f0c9b733afd41d47db02aa'
BASE_API_URL = 'https://service-testnet.maschain.com'

headers = {
    'client_id ': f'{API_KEY}',
    'client_secret': f'{API_PASSWORD}',
    'content-type': 'application/json'
}

def test_api_token():
    response = requests.get(BASE_API_URL, headers=headers)
    if response.status_code == 200:
        return JsonResponse({'status': 'success'})
    else:
        # Handle errors
        print('Error:', response.status_code, response.text)

# Temporarily allow GET requests for testing
@require_http_methods(["GET", "POST"])
def mint_token(request):
    API_URL = f'{BASE_API_URL}'

    try:
        response = requests.post(API_URL, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        
        if response.status_code == 200:
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': response.text}, status=response.status_code)
    
    except requests.exceptions.HTTPError as http_err:
        return JsonResponse({'status': 'error', 'message': f'HTTP error occurred: {http_err}'}, status=500)
    except requests.exceptions.ConnectionError as conn_err:
        return JsonResponse({'status': 'error', 'message': f'Connection error occurred: {conn_err}'}, status=500)
    except requests.exceptions.Timeout as timeout_err:
        return JsonResponse({'status': 'error', 'message': f'Timeout error occurred: {timeout_err}'}, status=500)
    except requests.exceptions.RequestException as req_err:
        return JsonResponse({'status': 'error', 'message': f'An error occurred: {req_err}'}, status=500)
