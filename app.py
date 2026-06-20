from flask import Flask, request
import requests

app = Flask(__name__)

# ===== TELEGRAM CONFIG =====
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, data=data)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    symbol = data.get("symbol", "N/A")
    signal = data.get("signal", "N/A")
    price = data.get("price", "N/A")

    msg = f"""
📊 TRADE SIGNAL

PAIR: {symbol}
ACTION: {signal}
PRICE: {price}

⚡ Manual MT5 entry
"""

    send_telegram(msg)
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(port=5000)
