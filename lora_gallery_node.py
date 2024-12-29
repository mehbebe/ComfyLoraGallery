from flask import Flask, jsonify, render_template, request
import os
from safetensors.torch import load_file

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("lora_gallery.html")

@app.route("/get_loras", methods=["GET"])
def get_loras():
    lora_directory = request.args.get("directory", "./Models/loras")
    if not os.path.exists(lora_directory):
        return jsonify({"error": "Directory not found"}), 404

    lora_files = [
        f for f in os.listdir(lora_directory) if f.endswith(('.safetensors', '.pt'))
    ]
    if not lora_files:
        return jsonify({"error": "No LoRAs found"}), 404

    lora_data = []
    for lora in lora_files:
        lora_path = os.path.join(lora_directory, lora)
        preview_path = os.path.splitext(lora_path)[0] + ".png"

        try:
            metadata = load_file(lora_path)
            trigger_word = metadata.get("additional_network_kwargs", {}).get("trigger_word", "No trigger words found")
            base_model = "SDXL 1.0" if "SDXL" in lora_path else "SD1.5"
        except Exception:
            trigger_word = "Error reading metadata"
            base_model = "Unknown"

        lora_data.append({
            "name": lora,
            "preview": preview_path if os.path.exists(preview_path) else "",
            "trigger_word": trigger_word,
            "base_model": base_model,
        })

    return jsonify(lora_data)
