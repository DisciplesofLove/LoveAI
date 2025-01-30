import requests
import json

def route_data(data, node_url):
    """Sends AI task data to a compute node."""
    try:
        response = requests.post(f"{node_url}/inference", json={"text": data})
        return response.json()
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    data = "Explain decentralized AI"
    node_url = "http://node1:5000"
    result = route_data(data, node_url)
    print("AI Response:", result)
