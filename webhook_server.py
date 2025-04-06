from flask import Flask, request, jsonify
from trading_bot import execute_trade

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("📩 Webhook erhalten:", data)

    if data and 'action' in data:
        action = data['action']
        execute_trade(action)
        return jsonify({"status": "erhalten", "nachricht": f"{action}-Signal verarbeitet"}), 200
    else:
        return jsonify({"status": "fehler", "nachricht": "Ungültiges Format"}), 400
