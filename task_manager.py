from flask import Flask, request, jsonify
import requests
import random

app = Flask(__name__)

# List of available compute nodes (example IPs, replace with actual nodes)
COMPUTE_NODES = [
    "http://node1:5000/inference",
    "http://node2:5000/inference",
    "http://node3:5000/inference"
]

# Select a compute node (random for now, can be optimized later)
def select_compute_node():
    return random.choice(COMPUTE_NODES)

@app.route('/task', methods=['POST'])
def handle_task():
    data = request.json
    input_text = data.get("text", "")
    compute_node = select_compute_node()
    
    try:
        response = requests.post(compute_node, json={"text": input_text})
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
