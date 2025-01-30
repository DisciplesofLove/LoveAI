import json
import hashlib

# Load metadata
def load_metadata(metadata_file):
    with open(metadata_file, 'r') as f:
        return json.load(f)

# Generate Merkle Tree root from chunk hashes
def compute_merkle_root(chunk_hashes):
    while len(chunk_hashes) > 1:
        chunk_hashes = [hashlib.sha256((chunk_hashes[i] + chunk_hashes[i+1]).encode()).hexdigest()
                        for i in range(0, len(chunk_hashes)-1, 2)]
    return chunk_hashes[0]

# Example usage
metadata = load_metadata("model_metadata.json")
chunk_hashes = [chunk["hash"] for chunk in metadata["chunks"]]
merkle_root = compute_merkle_root(chunk_hashes)
print(f"Merkle Root: {merkle_root}")
