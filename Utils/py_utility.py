import requests
from cryptography.fernet import Fernet

def getPublicIp() -> str:
    response = requests.get('https://api.ipify.org')
    public_ip = response.text
    return public_ip

def decryptData(data: bytes, key: bytes) -> bytes:
    """
    Decrypts data using Fernet decryption.

    Args:
        data (bytes): The data to decrypt.
        key (bytes): The encryption key.

    Returns:
        bytes: The decrypted data.
    """
    cipher = Fernet(key)
    decrypted_data = cipher.decrypt(data)
    return decrypted_data