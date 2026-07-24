import json
import os


def save_history(total_value, total_profit, overall_return):

    history_file = "history.json"

    if os.path.exists(history_file):
        with open(history_file, "r") as file:
            history = json.load(file)
    else:
        history = []

    from datetime import datetime

    today = datetime.now().strftime("%Y-%m-%d")

    # Don't create duplicate entries for the same day
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

    with open(history_file, "r") as file:
     print(file.read())
     file.seek(0)
     history = json.load(file)

     print(history)
     print(type(history))