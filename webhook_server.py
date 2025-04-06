from flask import Flask, request, jsonify
from trading_bot import execute_trade
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("📩 Webhook empfangen:", data)

    if data and 'action' in data:
        action = data['action']
        execute_trade(action)
        return jsonify({"status": "erhalten", "nachricht": f"{action}-Signal verarbeitet"}), 200
    else:
        return jsonify({"status": "fehler", "nachricht": "Ungültiges Format"}), 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

