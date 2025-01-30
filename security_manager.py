import hashlib
import os

SECRET_KEY = os.getenv("SECRET_KEY", "default-secret")

def encrypt_data(data):
    """Encrypts data using a simple hash-based method."""
    return hashlib.sha256((data + SECRET_KEY).encode()).hexdigest()

def verify_data(data, encrypted_hash):
    """Verifies that the encrypted data matches the original hash."""
    return encrypt_data(data) == encrypted_hash

# Example Usage
if __name__ == "__main__":
    text = "Secure AI communication"
    encrypted = encrypt_data(text)
    print(f"Encrypted Data: {encrypted}")

    is_valid = verify_data(text, encrypted)
    print(f"Verification Successful: {is_valid}")
