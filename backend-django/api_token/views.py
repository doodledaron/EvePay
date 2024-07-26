import requests
from django.http import JsonResponse
from rest_framework.decorators import api_view
import logging
from api_wallet.views import get_wallet_adrr
from utils import convert_to_readable_timestamp

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

# Token API_KEY and API_PASSWORD
API_KEY = 'd2e5b49b8d126cd2687d9c61b8f6ba2e64e856d6c34cdf27fb3cb9b59bd2d2a3'
API_PASSWORD = 'sk_43375ea6665657b0030e702f30144c664239d43c03f0c9b733afd41d47db02aa'
BASE_API_URL = 'https://service-testnet.maschain.com/api/token'

# Headers Credentials For Maschain API
headers = {
    'client_id': f'{API_KEY}',
    'client_secret': f'{API_PASSWORD}',
    'content-type': 'application/json'
}

# Function to calculate the charge fee
def calculate_charge(capacity_used):
    charge_rate = 1.25
    return charge_rate * capacity_used

# Test API Token Connection
def test_api_token_conn(request):
    response = requests.get(BASE_API_URL, headers=headers)
    if response.status_code == 200:
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': response.text}, status=response.status_code)

# Mint Token
@api_view(['POST'])
def mint_token(request):
    API_URL = f'{BASE_API_URL}/mint'

    try:
        # Get data from the request body
        data = request.data
        logger.debug(f"Request Data: {data}")
        
        # Make the POST request to the external API with the data
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        
        if response.status_code == 200:
            logger.debug(f"Response Data: {response.json()}")
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

# Pause Token
@api_view(['POST'])
def pause_token(request):
    API_URL = f'{BASE_API_URL}/pause'

    try:
        # Get data from the request body
        data = request.data
        logger.debug(f"Request Data: {data}")
        
        # Make the POST request to the external API with the data
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        
        if response.status_code == 200:
            logger.debug(f"Response Data: {response.json()}")
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

# Resume Token
@api_view(['POST'])
def resume_token(request):
    API_URL = f'{BASE_API_URL}/resume'

    try:
        # Get data from the request body
        data = request.data
        logger.debug(f"Request Data: {data}")
        
        # Make the POST request to the external API with the data
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        
        if response.status_code == 200:
            logger.debug(f"Response Data: {response.json()}")
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

# Burn Token
@api_view(['POST'])
def burn_token(request):
    API_URL = f'{BASE_API_URL}/burn'

    try:
        # Get data from the request body
        data = request.data
        logger.debug(f"Request Data: {data}")
        
        # Make the POST request to the external API with the data
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        
        if response.status_code == 200:
            logger.debug(f"Response Data: {response.json()}")
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

# Transfer Token
@api_view(['POST'])
def transfer_token(request, capacity_used):
    API_URL = f'{BASE_API_URL}/token-transfer'

    try:
        # Get the charge token value
        charge_token = calculate_charge(capacity_used)
        
        # Get data from the request body
        data = request.data

        # Update the amount field with the charge token value
        data['amount'] = charge_token 
        # data['callback_url'] = 'http://localhost:8000/maschain_token/callback-handler/' 
        logger.debug(f"Request Data: {data}")
           
        # Make the POST request to the external API with the data
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        
        if response.status_code == 200:
            logger.debug(f"Response Data: {response.json()}")
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
    
# Trasnfer Owner Wallet
@api_view(['POST'])
def transfer_owner(request):
    API_URL = f'{BASE_API_URL}/owner-transfer'

    try:
        # Get data from the request body
        data = request.data
        logger.debug(f"Request Data: {data}")
        
        # Make the POST request to the external API with the data
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        
        if response.status_code == 200:
            logger.debug(f"Response Data: {response.json()}")
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


def check_balance(request):
    API_URL = f'{BASE_API_URL}/balance'

    try:
        # Get data from the request body
        data = request.data
        logger.debug(f"Request Data: {data}")
        
        # Make the POST request to the external API with the data
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        
        if response.status_code == 200:
            logger.debug(f"Response Data: {response.json()}")
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

# Get Transaction Filter To
@api_view(['GET'])
def get_transaction_filter_to(request, wallet_address):
    """
    Fetch the list of transaction from the external API.
    
    Returns:
        JsonResponse: A JSON response with the status and data or error message.
    """

    API_URL = f'{BASE_API_URL}/get-token-transaction'
    contract_address = '0xA10b5960afae880bA86cb3Bb5ec1Ae2eBAe19083'
    params = {
        'wallet_address': f'{wallet_address}',
        'contract_address': f'{contract_address}',
        'filter': "to"
    }

    try:
        # Make the GET request to the external API
        response = requests.get(API_URL, headers=headers, params=params)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)

        if response.status_code == 200:
            data = response.json()
            for transaction in data.get('result', []):
                from_address = transaction.get('from')
                to_address = transaction.get('to')
                timestamp = transaction.get('timestamp')
                amount = transaction.get('amount')
                if from_address:
                    from_details = get_wallet_adrr(from_address)
                    transaction['from'] = from_details.get('result', {}).get('name', 'Unknown')
                if to_address:
                    to_details = get_wallet_adrr(to_address)
                    transaction['to'] = to_details.get('result', {}).get('name', 'Unknown')
                if timestamp:
                    readable_timestamp = convert_to_readable_timestamp(timestamp)
                    # logger.debug(f"Readable Timestamp: {readable_timestamp}")
                    transaction['timestamp'] = readable_timestamp
                if amount:
                    transaction['amount'] = f'{float(amount) / 100:.2f} EVEC'
            return JsonResponse({'status': 'success', 'data': data})
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

# Get Transaction Filter From
@api_view(['GET'])
def get_transaction_filter_from(request, wallet_address):
    """
    Fetch the list of transaction from the external API.
    
    Returns:
        JsonResponse: A JSON response with the status and data or error message.
    """

    API_URL = f'{BASE_API_URL}/get-token-transaction'
    contract_address = '0xA10b5960afae880bA86cb3Bb5ec1Ae2eBAe19083'
    params = {
        'wallet_address': f'{wallet_address}',
        'contract_address': f'{contract_address}',
        'filter': "from"
    }

    try:
        # Make the GET request to the external API
        response = requests.get(API_URL, headers=headers, params=params)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)

        if response.status_code == 200:
            data = response.json()
            for transaction in data.get('result', []):
                from_address = transaction.get('from')
                to_address = transaction.get('to')
                timestamp = transaction.get('timestamp')
                amount = transaction.get('amount')
                if from_address:
                    from_details = get_wallet_adrr(from_address)
                    transaction['from'] = from_details.get('result', {}).get('name', 'Unknown')
                if to_address:
                    to_details = get_wallet_adrr(to_address)
                    transaction['to'] = to_details.get('result', {}).get('name', 'Unknown')
                if timestamp:
                    readable_timestamp = convert_to_readable_timestamp(timestamp)
                    # logger.debug(f"Readable Timestamp: {readable_timestamp}")
                    transaction['timestamp'] = readable_timestamp
                if amount:
                    transaction['amount'] = f'{float(amount) / 100:.2f} EVEC'

            return JsonResponse({'status': 'success', 'data': data})
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
    
# Callback Handler
@api_view(['POST'])
def callback_handler(request):
    try:
        # Get data from the request body
        data = request.data
        logger.debug(f"Callback Data: {data}")

        # Process the callback data
        status = data.get('status')
        result = data.get('result')

        if result:
            transaction_hash = result.get('transactionHash')
            nonce = result.get('nonce')
            from_address = result.get('from')
            status = result.get('status')
            receipt = result.get('receipt')
            
            # Here, you would add logic to update your database or perform other actions based on the callback data
            # update_transaction_status(transaction_hash, nonce, from_address, status, receipt)
            
            # Log the callback response
            logger.info(f"Processed callback for transaction hash: {transaction_hash} with status: {status}")

        return JsonResponse({'status': 'success', 'message': 'Callback processed successfully'})

    except Exception as e:
        logger.error(f"Error processing callback: {e}")
        return JsonResponse({'status': 'error', 'message': f'Error processing callback: {e}'}, status=500)