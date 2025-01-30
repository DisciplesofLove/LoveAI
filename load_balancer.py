from flask import Flask, request, jsonify
import requests
import random

app = Flask(__name__)

# List of available compute nodes (example IPs, replace with actual nodes)
COMPUTE_NODES = [
    {"url": "http://node1:5000/inference", "load": 0},
    {"url": "http://node2:5000/inference", "load": 0},
    {"url": "http://node3:5000/inference", "load": 0}
]

# Select the least loaded compute node
def select_best_node():
    best_node = min(COMPUTE_NODES, key=lambda node: node["load"])
    best_node["load"] += 1  # Simulate load increment
    return best_node["url"]

@app.route('/route-task', methods=['POST'])
def route_task():
    data = request.json
    input_text = data.get("text", "")
    best_node = select_best_node()
    
    try:
        response = requests.post(best_node, json={"text": input_text})
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9000)
