from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, jsonify
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import random
import torch

tokenizer = GPT2Tokenizer.from_pretrained("gpt2-medium")
model = GPT2LMHeadModel.from_pretrained("gpt2-medium")

latest_news = []


def generate_news():
    global latest_news
    text = "Rick and Morty"
    inputs = tokenizer.encode(text, return_tensors="pt")
    outputs = model.generate(
        inputs,
        temperature=0.9,
        max_length=95,
        do_sample=True
    )
    output = tokenizer.decode(outputs[0], skip_special_tokens=False)

    formatted_text = output.replace('"', '')
    latest_news.append(formatted_text)
    print(len(latest_news))


scheduler = BackgroundScheduler()
scheduler.add_job(generate_news, 'interval', minutes=random.randint(1, 2))
scheduler.start()

app = Flask(__name__)


@app.route('/latest-news', methods=['GET'])
def get_latest_news():
    return jsonify({'news': latest_news})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)
