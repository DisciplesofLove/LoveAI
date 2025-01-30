import ipfshttpclient
import json

def upload_to_ipfs(file_path):
    """Uploads a file to IPFS and returns the CID."""
    client = ipfshttpclient.connect()
    res = client.add(file_path)
    return res["Hash"]

def store_chunks_in_ipfs(metadata_file):
    """Uploads all model chunks to IPFS and updates metadata with CIDs."""
    with open(metadata_file, "r") as f:
        metadata = json.load(f)

    for chunk in metadata["chunks"]:
        chunk["cid"] = upload_to_ipfs(f"model_chunks/{chunk['chunk_id']}")
        print(f"Uploaded {chunk['chunk_id']} to IPFS: {chunk['cid']}")

    with open(metadata_file, "w") as f:
        json.dump(metadata, f, indent=4)

if __name__ == "__main__":
    store_chunks_in_ipfs("model_metadata.json")
