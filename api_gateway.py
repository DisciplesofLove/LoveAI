from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

LOAD_BALANCER_URL = "http://localhost:9000/route-task"

@app.route('/ai-request', methods=['POST'])
def process_ai_request():
    """Receives an AI request and forwards it to the load balancer."""
    data = request.json
    try:
        response = requests.post(LOAD_BALANCER_URL, json=data)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
