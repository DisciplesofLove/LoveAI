import ipfshttpclient
import hashlib
import json
import os

MODEL_DIR = "reconstructed_model"

def fetch_from_ipfs(cid, output_path):
    """Fetches a chunk from IPFS and saves it locally."""
    client = ipfshttpclient.connect()
    data = client.cat(cid)
    with open(output_path, "wb") as f:
        f.write(data)

def verify_chunk(chunk_path, expected_hash):
    """Verifies chunk integrity using SHA-256 hash."""
    sha256 = hashlib.sha256(open(chunk_path, "rb").read()).hexdigest()
    return sha256 == expected_hash

def reassemble_model(metadata_file):
    """Fetches and verifies model chunks, then reconstructs the full model."""
    os.makedirs(MODEL_DIR, exist_ok=True)
    
    with open(metadata_file, "r") as f:
        metadata = json.load(f)

    for chunk in metadata["chunks"]:
        chunk_path = os.path.join(MODEL_DIR, chunk["chunk_id"])
        fetch_from_ipfs(chunk["cid"], chunk_path)

        if not verify_chunk(chunk_path, chunk["hash"]):
            raise ValueError(f"Integrity check failed for {chunk['chunk_id']}")

    print("All chunks verified. Reassembling model...")
    with open(os.path.join(MODEL_DIR, "model.bin"), "wb") as f_out:
        for chunk in metadata["chunks"]:
            with open(os.path.join(MODEL_DIR, chunk["chunk_id"]), "rb") as f_in:
                f_out.write(f_in.read())

if __name__ == "__main__":
    reassemble_model("model_metadata.json")
