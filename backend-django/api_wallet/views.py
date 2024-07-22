# import requests
# from django.http import JsonResponse

# def api_token(request):
#     API_KEY = 'd2e5b49b8d126cd2687d9c61b8f6ba2e64e856d6c34cdf27fb3cb9b59bd2d2a3'
#     API_URL = 'https://service-testnet.maschain.com'

#     headers = {
#         'Authorization': f'Bearer {API_KEY}',
#         'Content-Type': 'application/json'
#     }

#     response = requests.get(API_URL, headers=headers)
#     if response.status_code == 200:
#         # Success
#         data = response.json()
#         print('Response Data:', data)
#     else:
#         # Handle errors
#         print('Error:', response.status_code, response.text)
