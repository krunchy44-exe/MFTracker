import json
import os
from datetime import datetime


def save_history(total_value, total_profit, overall_return):

    history_file = "history.json"

    if os.path.exists(history_file):
        with open(history_file, "r") as file:
            history = json.load(file)
    else:
        history = []

    today = datetime.now().strftime("%Y-%m-%d")

    # Update today's entry if it already exists
    if history and history[-1]["date"] == today:
        history[-1] = {
            "date": today,
            "portfolio_value": total_value,
            "profit": total_profit,
            "return": overall_return
        }
    else:
        history.append({
            "date": today,
            "portfolio_value": total_value,
            "profit": total_profit,
            "return": overall_return
        })

    # ✅ Save updated history back to the file
    with open(history_file, "w") as file:
        json.dump(history, file, indent=4)

    print("History saved successfully!")