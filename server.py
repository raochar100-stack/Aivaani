from flask import Flask, request, jsonify
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "AI Vaani server is running!"

@app.route('/speak', methods=['POST'])
def speak():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    tts = gTTS(text=text, lang='hi')
    filename = "output.mp3"
    tts.save(filename)

    return jsonify({"message": "Speech generated", "file": filename})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
