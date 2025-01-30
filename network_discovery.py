import requests
import json

NODE_REGISTRY_URL = "http://node-registry-service.com/nodes"

def get_available_nodes():
    """Fetches a list of available compute nodes from the registry."""
    try:
        response = requests.get(NODE_REGISTRY_URL)
        if response.status_code == 200:
            return response.json()["nodes"]
        else:
            return []
    except Exception as e:
        print(f"Error fetching nodes: {e}")
        return []

if __name__ == "__main__":
    nodes = get_available_nodes()
    print("Available Compute Nodes:", nodes)
