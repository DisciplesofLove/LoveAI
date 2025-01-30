import os
import hashlib
import json
import shutil

CHUNK_SIZE = 256 * 1024 * 1024  # 256MB per chunk

def split_model(model_path, output_dir):
    """Splits the DeepSeek V3 model into smaller chunks for decentralized storage."""
    os.makedirs(output_dir, exist_ok=True)
    chunk_paths = []
    
    with open(model_path, 'rb') as f:
        chunk_index = 0
        while chunk := f.read(CHUNK_SIZE):
            chunk_name = os.path.join(output_dir, f"chunk_{chunk_index:03}.bin")
            with open(chunk_name, 'wb') as chunk_file:
                chunk_file.write(chunk)
            chunk_paths.append(chunk_name)
            chunk_index += 1

    print(f"Model split into {chunk_index} chunks.")
    return chunk_paths

def generate_metadata(chunk_paths):
    """Generates metadata for model chunks with SHA-256 hashes."""
    metadata = {"chunks": []}
    for chunk_path in chunk_paths:
        chunk_hash = hashlib.sha256(open(chunk_path, 'rb').read()).hexdigest()
        metadata["chunks"].append({"chunk_id": os.path.basename(chunk_path), "hash": chunk_hash})

    with open("model_metadata.json", "w") as f:
        json.dump(metadata, f, indent=4)

if __name__ == "__main__":
    model_path = "DeepSeek-V3/weights.bin"
    output_dir = "model_chunks"
    chunk_paths = split_model(model_path, output_dir)
    generate_metadata(chunk_paths)
