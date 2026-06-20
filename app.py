from flask import Flask, request
import requests
import os

app = Flask(__name__)

TOKEN = os.environ.get("TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": message})

@app.route("/")
def home():
    return "Bot Running OK 🚀"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json or {}

    symbol = data.get("symbol", "N/A")
    signal = data.get("signal", "N/A")
    price = data.get("price", "N/A")

    send_telegram(f"PAIR: {symbol}\nSIGNAL: {signal}\nPRICE: {price}")
    return {"status": "ok"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))   # 👈 IMPORTANT FIX
    app.run(host="0.0.0.0", port=port)
