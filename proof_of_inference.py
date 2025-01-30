import hashlib

# Generate proof of inference
def generate_poi(input_text, output_text):
    return hashlib.sha256((input_text + output_text).encode()).hexdigest()

# Verify proof
def verify_poi(input_text, output_text, provided_poi):
    computed_poi = generate_poi(input_text, output_text)
    return computed_poi == provided_poi
