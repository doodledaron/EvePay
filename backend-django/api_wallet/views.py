import requests
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.utils.decorators import method_decorator
import logging

# logger configuration
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Wallet API_KEY and API_PASSWORD
API_KEY = '1f72c3ffa1b76eba742c3371656447d7e09ec8e208405563f0ed0c89afcbe33e'
API_PASSWORD = 'sk_b8f75bc49cc51499702fa7d43c07ef8465ad881cad21e73e585344a8e92faccd'
BASE_API_URL = 'https://service-testnet.maschain.com/api/wallet'

headers = {
    'client_id': f'{API_KEY}',
    'client_secret': f'{API_PASSWORD}',
    'content-type': 'application/json'
}

def test_api_wallet_conn(request):
    response = requests.get(BASE_API_URL, headers=headers)
    if response.status_code == 200:
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': response.text}, status=response.status_code)

@api_view(['POST'])
def create_orgainsation_wallet(request):
    API_URL = f'{BASE_API_URL}/wallet'

    try:
        # Get data from the request body
        data = request.data
        logger.debug(f"Request Data: {data}")
        
        # Make the POST request to the external API with the data
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        
        if response.status_code == 200:
            return JsonResponse({'status': 'success', 'data': response.json()})
        else:
            return JsonResponse({'status': 'error', 'message': response.text}, status=response.status_code)
    
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err} - {response.status_code} - {response.text}")
        return JsonResponse({'status': 'error', 'message': f'HTTP error occurred: {http_err}'}, status=500)
    except requests.exceptions.ConnectionError as conn_err:
        logger.error(f"Connection error occurred: {conn_err}")
        return JsonResponse({'status': 'error', 'message': f'Connection error occurred: {conn_err}'}, status=500)
    except requests.exceptions.Timeout as timeout_err:
        logger.error(f"Timeout error occurred: {timeout_err}")
        return JsonResponse({'status': 'error', 'message': f'Timeout error occurred: {timeout_err}'}, status=500)
    except requests.exceptions.RequestException as req_err:
        logger.error(f"An error occurred: {req_err}")
        return JsonResponse({'status': 'error', 'message': f'An error occurred: {req_err}'}, status=500)
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")
        return JsonResponse({'status': 'error', 'message': f'Unexpected error occurred: {e}'}, status=500)

@api_view(['POST'])
def create_user_wallet(request):
    API_URL = f'{BASE_API_URL}/create-user'

    try:
        # Get data from the request body
        data = request.data
        logger.debug(f"Request Data: {data}")
        
        # Make the POST request to the external API with the data
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        
        if response.status_code == 200:
            return JsonResponse({'status': 'success', 'data': response.json()})
        else:
            return JsonResponse({'status': 'error', 'message': response.text}, status=response.status_code)
    
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err} - {response.status_code} - {response.text}")
        return JsonResponse({'status': 'error', 'message': f'HTTP error occurred: {http_err}'}, status=500)
    except requests.exceptions.ConnectionError as conn_err:
        logger.error(f"Connection error occurred: {conn_err}")
        return JsonResponse({'status': 'error', 'message': f'Connection error occurred: {conn_err}'}, status=500)
    except requests.exceptions.Timeout as timeout_err:
        logger.error(f"Timeout error occurred: {timeout_err}")
        return JsonResponse({'status': 'error', 'message': f'Timeout error occurred: {timeout_err}'}, status=500)
    except requests.exceptions.RequestException as req_err:
        logger.error(f"An error occurred: {req_err}")
        return JsonResponse({'status': 'error', 'message': f'An error occurred: {req_err}'}, status=500)
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")
        return JsonResponse({'status': 'error', 'message': f'Unexpected error occurred: {e}'}, status=500)

@api_view(['POST'])
def create_entity(request):
    API_URL = f'{BASE_API_URL}/entity'

    try:
        # Get data from the request body
        data = request.data
        logger.debug(f"Request Data: {data}")
        
        # Make the POST request to the external API with the data
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        
        if response.status_code == 200:
            return JsonResponse({'status': 'success', 'data': response.json()})
        else:
            return JsonResponse({'status': 'error', 'message': response.text}, status=response.status_code)
    
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err} - {response.status_code} - {response.text}")
        return JsonResponse({'status': 'error', 'message': f'HTTP error occurred: {http_err}'}, status=500)
    except requests.exceptions.ConnectionError as conn_err:
        logger.error(f"Connection error occurred: {conn_err}")
        return JsonResponse({'status': 'error', 'message': f'Connection error occurred: {conn_err}'}, status=500)
    except requests.exceptions.Timeout as timeout_err:
        logger.error(f"Timeout error occurred: {timeout_err}")
        return JsonResponse({'status': 'error', 'message': f'Timeout error occurred: {timeout_err}'}, status=500)
    except requests.exceptions.RequestException as req_err:
        logger.error(f"An error occurred: {req_err}")
        return JsonResponse({'status': 'error', 'message': f'An error occurred: {req_err}'}, status=500)
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")
        return JsonResponse({'status': 'error', 'message': f'Unexpected error occurred: {e}'}, status=500)

@api_view(['POST'])
def create_entity_category(request):

    API_URL = f'{BASE_API_URL}/entity-category'

    try:
        # Get data from the request body
        data = request.data
        logger.debug(f"Request Data: {data}")
        
        # Make the POST request to the external API with the data
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        
        if response.status_code == 200:
            return JsonResponse({'status': 'success', 'data': response.json()})
        else:
            return JsonResponse({'status': 'error', 'message': response.text}, status=response.status_code)
    
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err} - {response.status_code} - {response.text}")
        return JsonResponse({'status': 'error', 'message': f'HTTP error occurred: {http_err}'}, status=500)
    except requests.exceptions.ConnectionError as conn_err:
        logger.error(f"Connection error occurred: {conn_err}")
        return JsonResponse({'status': 'error', 'message': f'Connection error occurred: {conn_err}'}, status=500)
    except requests.exceptions.Timeout as timeout_err:
        logger.error(f"Timeout error occurred: {timeout_err}")
        return JsonResponse({'status': 'error', 'message': f'Timeout error occurred: {timeout_err}'}, status=500)
    except requests.exceptions.RequestException as req_err:
        logger.error(f"An error occurred: {req_err}")
        return JsonResponse({'status': 'error', 'message': f'An error occurred: {req_err}'}, status=500)
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")
        return JsonResponse({'status': 'error', 'message': f'Unexpected error occurred: {e}'}, status=500)
    

    API_URL = f'{BASE_API_URL}/entity'

    try:
        # Get data from the request body
        data = request.data
        logger.debug(f"Request Data: {data}")
        
        # Make the POST request to the external API with the data
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        
        if response.status_code == 200:
            return JsonResponse({'status': 'success', 'data': response.json()})
        else:
            return JsonResponse({'status': 'error', 'message': response.text}, status=response.status_code)
    
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err} - {response.status_code} - {response.text}")
        return JsonResponse({'status': 'error', 'message': f'HTTP error occurred: {http_err}'}, status=500)
    except requests.exceptions.ConnectionError as conn_err:
        logger.error(f"Connection error occurred: {conn_err}")
        return JsonResponse({'status': 'error', 'message': f'Connection error occurred: {conn_err}'}, status=500)
    except requests.exceptions.Timeout as timeout_err:
        logger.error(f"Timeout error occurred: {timeout_err}")
        return JsonResponse({'status': 'error', 'message': f'Timeout error occurred: {timeout_err}'}, status=500)
    except requests.exceptions.RequestException as req_err:
        logger.error(f"An error occurred: {req_err}")
        return JsonResponse({'status': 'error', 'message': f'An error occurred: {req_err}'}, status=500)
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")
        return JsonResponse({'status': 'error', 'message': f'Unexpected error occurred: {e}'}, status=500)

@api_view(['POST'])
def create_wallet_category(request):

    API_URL = f'{BASE_API_URL}/wallet-category'

    try:
        # Get data from the request body
        data = request.data
        logger.debug(f"Request Data: {data}")
        
        # Make the POST request to the external API with the data
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        
        if response.status_code == 200:
            return JsonResponse({'status': 'success', 'data': response.json()})
        else:
            return JsonResponse({'status': 'error', 'message': response.text}, status=response.status_code)
    
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err} - {response.status_code} - {response.text}")
        return JsonResponse({'status': 'error', 'message': f'HTTP error occurred: {http_err}'}, status=500)
    except requests.exceptions.ConnectionError as conn_err:
        logger.error(f"Connection error occurred: {conn_err}")
        return JsonResponse({'status': 'error', 'message': f'Connection error occurred: {conn_err}'}, status=500)
    except requests.exceptions.Timeout as timeout_err:
        logger.error(f"Timeout error occurred: {timeout_err}")
        return JsonResponse({'status': 'error', 'message': f'Timeout error occurred: {timeout_err}'}, status=500)
    except requests.exceptions.RequestException as req_err:
        logger.error(f"An error occurred: {req_err}")
        return JsonResponse({'status': 'error', 'message': f'An error occurred: {req_err}'}, status=500)
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")
        return JsonResponse({'status': 'error', 'message': f'Unexpected error occurred: {e}'}, status=500)

@api_view(['GET'])
def get_entity_list(request):
    """
    Fetch the list of entities from the external API.
    
    Returns:
        JsonResponse: A JSON response with the status and data or error message.
    """

    API_URL = f'{BASE_API_URL}/entity'

    try:
        # Make the GET request to the external API
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        
        if response.status_code == 200:
            return JsonResponse({'status': 'success', 'data': response.json()})
        else:
            return JsonResponse({'status': 'error', 'message': response.text}, status=response.status_code)
    
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err} - {response.status_code} - {response.text}")
        return JsonResponse({'status': 'error', 'message': f'HTTP error occurred: {http_err}'}, status=500)
    except requests.exceptions.ConnectionError as conn_err:
        logger.error(f"Connection error occurred: {conn_err}")
        return JsonResponse({'status': 'error', 'message': f'Connection error occurred: {conn_err}'}, status=500)
    except requests.exceptions.Timeout as timeout_err:
        logger.error(f"Timeout error occurred: {timeout_err}")
        return JsonResponse({'status': 'error', 'message': f'Timeout error occurred: {timeout_err}'}, status=500)
    except requests.exceptions.RequestException as req_err:
        logger.error(f"An error occurred: {req_err}")
        return JsonResponse({'status': 'error', 'message': f'An error occurred: {req_err}'}, status=500)
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")
        return JsonResponse({'status': 'error', 'message': f'Unexpected error occurred: {e}'}, status=500)

@api_view(['GET'])
def get_cat_entity_list(request):
    """
    Fetch the list of entities from the external API.
    
    Returns:
        JsonResponse: A JSON response with the status and data or error message.
    """

    API_URL = f'{BASE_API_URL}/entity-category'

    try:
        # Make the GET request to the external API
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        
        if response.status_code == 200:
            return JsonResponse({'status': 'success', 'data': response.json()})
        else:
            return JsonResponse({'status': 'error', 'message': response.text}, status=response.status_code)
    
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err} - {response.status_code} - {response.text}")
        return JsonResponse({'status': 'error', 'message': f'HTTP error occurred: {http_err}'}, status=500)
    except requests.exceptions.ConnectionError as conn_err:
        logger.error(f"Connection error occurred: {conn_err}")
        return JsonResponse({'status': 'error', 'message': f'Connection error occurred: {conn_err}'}, status=500)
    except requests.exceptions.Timeout as timeout_err:
        logger.error(f"Timeout error occurred: {timeout_err}")
        return JsonResponse({'status': 'error', 'message': f'Timeout error occurred: {timeout_err}'}, status=500)
    except requests.exceptions.RequestException as req_err:
        logger.error(f"An error occurred: {req_err}")
        return JsonResponse({'status': 'error', 'message': f'An error occurred: {req_err}'}, status=500)
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")
        return JsonResponse({'status': 'error', 'message': f'Unexpected error occurred: {e}'}, status=500)

@api_view(['GET'])
def get_org_wallet_list(request):
    """
    Fetch the list of entities from the external API.
    
    Returns:
        JsonResponse: A JSON response with the status and data or error message.
    """

    API_URL = f'{BASE_API_URL}/wallet?type=1'

    try:
        # Make the GET request to the external API
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        
        if response.status_code == 200:
            return JsonResponse({'status': 'success', 'data': response.json()})
        else:
            return JsonResponse({'status': 'error', 'message': response.text}, status=response.status_code)
    
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err} - {response.status_code} - {response.text}")
        return JsonResponse({'status': 'error', 'message': f'HTTP error occurred: {http_err}'}, status=500)
    except requests.exceptions.ConnectionError as conn_err:
        logger.error(f"Connection error occurred: {conn_err}")
        return JsonResponse({'status': 'error', 'message': f'Connection error occurred: {conn_err}'}, status=500)
    except requests.exceptions.Timeout as timeout_err:
        logger.error(f"Timeout error occurred: {timeout_err}")
        return JsonResponse({'status': 'error', 'message': f'Timeout error occurred: {timeout_err}'}, status=500)
    except requests.exceptions.RequestException as req_err:
        logger.error(f"An error occurred: {req_err}")
        return JsonResponse({'status': 'error', 'message': f'An error occurred: {req_err}'}, status=500)
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")
        return JsonResponse({'status': 'error', 'message': f'Unexpected error occurred: {e}'}, status=500)

@api_view(['GET'])
def get_user_wallet_list(request):
    """
    Fetch the list of entities from the external API.
    
    Returns:
        JsonResponse: A JSON response with the status and data or error message.
    """

    API_URL = f'{BASE_API_URL}/wallet?type=2'

    try:
        # Make the GET request to the external API
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        
        if response.status_code == 200:
            return JsonResponse({'status': 'success', 'data': response.json()})
        else:
            return JsonResponse({'status': 'error', 'message': response.text}, status=response.status_code)
    
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err} - {response.status_code} - {response.text}")
        return JsonResponse({'status': 'error', 'message': f'HTTP error occurred: {http_err}'}, status=500)
    except requests.exceptions.ConnectionError as conn_err:
        logger.error(f"Connection error occurred: {conn_err}")
        return JsonResponse({'status': 'error', 'message': f'Connection error occurred: {conn_err}'}, status=500)
    except requests.exceptions.Timeout as timeout_err:
        logger.error(f"Timeout error occurred: {timeout_err}")
        return JsonResponse({'status': 'error', 'message': f'Timeout error occurred: {timeout_err}'}, status=500)
    except requests.exceptions.RequestException as req_err:
        logger.error(f"An error occurred: {req_err}")
        return JsonResponse({'status': 'error', 'message': f'An error occurred: {req_err}'}, status=500)
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")
        return JsonResponse({'status': 'error', 'message': f'Unexpected error occurred: {e}'}, status=500)

def get_wallet_adrr(address):
    """
    Fetch the wallet address details from the external API.
    
    Returns:
        dict: A dictionary with the status and data or error message.
    """
    API_URL = f'{BASE_API_URL}/wallet/{address}'

    try:
        # Make the GET request to the external API
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        
        if response.status_code == 200:
            return response.json()
        else:
            logger.error(f"Error fetching wallet address details: {response.text}")
            return {'status': 'error', 'message': response.text}
    
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err} - {response.status_code} - {response.text}")
        return {'status': 'error', 'message': f'HTTP error occurred: {http_err}'}
    except requests.exceptions.ConnectionError as conn_err:
        logger.error(f"Connection error occurred: {conn_err}")
        return {'status': 'error', 'message': f'Connection error occurred: {conn_err}'}
    except requests.exceptions.Timeout as timeout_err:
        logger.error(f"Timeout error occurred: {timeout_err}")
        return {'status': 'error', 'message': f'Timeout error occurred: {timeout_err}'}
    except requests.exceptions.RequestException as req_err:
        logger.error(f"An error occurred: {req_err}")
        return {'status': 'error', 'message': f'An error occurred: {req_err}'}
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")
        return {'status': 'error', 'message': f'Unexpected error occurred: {e}'}

@api_view(['GET'])
def get_wallet_transaction_count(request, address):
    """
    Fetch the list of entities from the external API.
    
    Returns:
        JsonResponse: A JSON response with the status and data or error message.
    """
    
    if not address:
        return JsonResponse({'status': 'error', 'message': 'Address parameter is required.'}, status=400)
    
    API_URL = f'{BASE_API_URL}/wallet/{address}/transactions-count?block=latest'

    try:
        # Make the GET request to the external API
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        
        if response.status_code == 200:
            return JsonResponse({'status': 'success', 'data': response.json()})
        else:
            return JsonResponse({'status': 'error', 'message': response.text}, status=response.status_code)
    
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err} - {response.status_code} - {response.text}")
        return JsonResponse({'status': 'error', 'message': f'HTTP error occurred: {http_err}'}, status=500)
    except requests.exceptions.ConnectionError as conn_err:
        logger.error(f"Connection error occurred: {conn_err}")
        return JsonResponse({'status': 'error', 'message': f'Connection error occurred: {conn_err}'}, status=500)
    except requests.exceptions.Timeout as timeout_err:
        logger.error(f"Timeout error occurred: {timeout_err}")
        return JsonResponse({'status': 'error', 'message': f'Timeout error occurred: {timeout_err}'}, status=500)
    except requests.exceptions.RequestException as req_err:
        logger.error(f"An error occurred: {req_err}")
        return JsonResponse({'status': 'error', 'message': f'An error occurred: {req_err}'}, status=500)
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")
        return JsonResponse({'status': 'error', 'message': f'Unexpected error occurred: {e}'}, status=500)

# 24/7/2024
# Problem - cannot send PUT request
@api_view(['PUT'])
def activate_wallet(request):
    """
    Fetch the list of entities from the external API.
    
    Returns:
        JsonResponse: A JSON response with the status and data or error message.
    """
    
    id = request.data.get('id')
    
    API_URL = f'{BASE_API_URL}/wallet/{id}/activate'

    try:
        # Make the GET request to the external API
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        
        if response.status_code == 200:
            return JsonResponse({'status': 'success', 'data': response.json()})
        else:
            return JsonResponse({'status': 'error', 'message': response.text}, status=response.status_code)
    
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err} - {response.status_code} - {response.text}")
        return JsonResponse({'status': 'error', 'message': f'HTTP error occurred: {http_err}'}, status=500)
    except requests.exceptions.ConnectionError as conn_err:
        logger.error(f"Connection error occurred: {conn_err}")
        return JsonResponse({'status': 'error', 'message': f'Connection error occurred: {conn_err}'}, status=500)
    except requests.exceptions.Timeout as timeout_err:
        logger.error(f"Timeout error occurred: {timeout_err}")
        return JsonResponse({'status': 'error', 'message': f'Timeout error occurred: {timeout_err}'}, status=500)
    except requests.exceptions.RequestException as req_err:
        logger.error(f"An error occurred: {req_err}")
        return JsonResponse({'status': 'error', 'message': f'An error occurred: {req_err}'}, status=500)
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")
        return JsonResponse({'status': 'error', 'message': f'Unexpected error occurred: {e}'}, status=500)

@api_view(['PUT'])
def deactivate_wallet(request):
    """
    Fetch the list of entities from the external API.
    
    Returns:
        JsonResponse: A JSON response with the status and data or error message.
    """
    
    if not id:
        return JsonResponse({'status': 'error', 'message': 'ID parameter is required.'}, status=400)
    
    API_URL = f'{BASE_API_URL}/wallet/{id}/activate'

    try:
        # Make the GET request to the external API
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        
        if response.status_code == 200:
            return JsonResponse({'status': 'success', 'data': response.json()})
        else:
            return JsonResponse({'status': 'error', 'message': response.text}, status=response.status_code)
    
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err} - {response.status_code} - {response.text}")
        return JsonResponse({'status': 'error', 'message': f'HTTP error occurred: {http_err}'}, status=500)
    except requests.exceptions.ConnectionError as conn_err:
        logger.error(f"Connection error occurred: {conn_err}")
        return JsonResponse({'status': 'error', 'message': f'Connection error occurred: {conn_err}'}, status=500)
    except requests.exceptions.Timeout as timeout_err:
        logger.error(f"Timeout error occurred: {timeout_err}")
        return JsonResponse({'status': 'error', 'message': f'Timeout error occurred: {timeout_err}'}, status=500)
    except requests.exceptions.RequestException as req_err:
        logger.error(f"An error occurred: {req_err}")
        return JsonResponse({'status': 'error', 'message': f'An error occurred: {req_err}'}, status=500)
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")
        return JsonResponse({'status': 'error', 'message': f'Unexpected error occurred: {e}'}, status=500)






