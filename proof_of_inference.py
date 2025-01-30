import hashlib
import json

def generate_proof(input_text, output_text):
    """Generates a Proof of Inference by hashing input and output together."""
    return hashlib.sha256((input_text + output_text).encode()).hexdigest()

def verify_proof(input_text, output_text, provided_proof):
    """Verifies the Proof of Inference by recalculating the hash and comparing it."""
    computed_proof = generate_proof(input_text, output_text)
    return computed_proof == provided_proof

# Example usage
def main():
    input_text = "What is decentralized AI?"
    output_text = "Decentralized AI removes control from centralized authorities..."
    
    proof = generate_proof(input_text, output_text)
    print(f"Generated Proof: {proof}")
    
    # Verification
    is_valid = verify_proof(input_text, output_text, proof)
    print(f"Proof is valid: {is_valid}")

if __name__ == "__main__":
    main()
