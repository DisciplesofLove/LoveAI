from flask import Flask, request, jsonify
from node_setup import run_inference

app = Flask(__name__)

@app.route('/inference', methods=['POST'])
def inference():
    data = request.json
    input_text = data.get("text", "")
    result = run_inference(input_text)
    return jsonify({"response": result})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
