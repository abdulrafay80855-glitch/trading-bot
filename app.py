from flask import Flask, request
import requests
import os

app = Flask(__name__)

TOKEN = os.environ.get("TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def send_telegram(msg):
    if TOKEN and CHAT_ID:
        requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            data={"chat_id": CHAT_ID, "text": msg}
        )

@app.route("/")
def home():
    return "Bot Running OK 🚀"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(force=True)

    symbol = data.get("symbol")
    signal = data.get("signal")
    price = data.get("price")

    send_telegram(f"{symbol} | {signal} | {price}")

    return {"status": "ok"}
