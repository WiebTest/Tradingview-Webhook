import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("📥 Webhook erhalten:")
    print(data)

    if data and 'action' in data:
        action = data['action']
        if action == 'buy':
            print("📈 Buy-Signal empfangen!")
        elif action == 'sell':
            print("📉 Sell-Signal empfangen!")
        else:
            print("❓ Unbekanntes Signal:", action)

    return jsonify({"status": "erhalten", "nachricht": "Webhook erfolgreich empfangen"}), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # <- Port wird dynamisch gesetzt
    app.run(host="0.0.0.0", port=port)
