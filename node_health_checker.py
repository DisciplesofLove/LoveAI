import requests
import time

COMPUTE_NODES = [
    {"url": "http://node1:5000", "status": "active"},
    {"url": "http://node2:5000", "status": "active"},
    {"url": "http://node3:5000", "status": "active"},
]

def check_node_health():
    """Checks each node to see if it's responsive."""
    for node in COMPUTE_NODES:
        try:
            response = requests.get(f"{node['url']}/health", timeout=3)
            if response.status_code == 200:
                node["status"] = "active"
            else:
                node["status"] = "inactive"
        except:
            node["status"] = "inactive"
    
    return [node for node in COMPUTE_NODES if node["status"] == "active"]

if __name__ == "__main__":
    while True:
        active_nodes = check_node_health()
        print(f"Active Nodes: {active_nodes}")
        time.sleep(10)  # Check every 10 seconds
