from flask import Flask, request, render_template
from summarizer import summarize_text, detokenize_text
from transformers import AutoTokenizer
import os
import socket
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("HUGGINGFACE_TOKEN") # for private models

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.form['input_text']
    tokenizer = AutoTokenizer.from_pretrained("t5-large")
    summary = summarize_text(text)
    cleaned_summary = detokenize_text(summary, tokenizer)
    return render_template('index.html', summary=cleaned_summary)

def find_free_port(starting_port=5000):
    port = starting_port
    while port <= 65535:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            result = s.connect_ex(('127.0.0.1', port))
            if result != 0: return port
            port += 1
    return None

if __name__ == "__main__":
    port = find_free_port()
    if port is not None:
        app.run(debug=True, port=port)
    else:
        print("Free port wasn't found.")
