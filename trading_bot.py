from datetime import datetime

def execute_trade(action):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if action == "buy":
        print(f"[{now}] ✅ SIMULIERTER TRADE: BUY ausgelöst.")
    elif action == "sell":
        print(f"[{now}] ✅ SIMULIERTER TRADE: SELL ausgelöst.")
    else:
        print(f"[{now}] ⚠️ Unbekannter Befehl erhalten: {action}")
