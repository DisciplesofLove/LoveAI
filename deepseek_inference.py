import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from flask import Flask, request, jsonify

MODEL_PATH = "reconstructed_model/model.bin"

app = Flask(__name__)

# Load the DeepSeek V3 Model
def load_model():
    print("Loading DeepSeek V3 model...")
    model = AutoModelForCausalLM.from_pretrained(MODEL_PATH)
    tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/deepseek-v3")
    return model, tokenizer

model, tokenizer = load_model()

# Run Inference
def run_inference(input_text):
    inputs = tokenizer(input_text, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=100)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

@app.route('/inference', methods=['POST'])
def inference():
    data = request.json
    input_text = data.get("text", "")
    result = run_inference(input_text)
    return jsonify({"response": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
