from datetime import datetime

def convert_to_readable_timestamp(timestamp):
    """
    Convert a timestamp to a more readable format.
    
    Args:
        timestamp (str): The original timestamp in ISO 8601 format.
    
    Returns:
        str: The readable timestamp.
    """
    
    dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
    return dt.strftime('%Y-%m-%d %H:%M:%S')