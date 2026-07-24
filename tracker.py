import json

from nav_fetcher import get_nav
from report_generator import create_report
from email_sender import send_email
from history_manager import save_history


def main():
    # Load portfolio
    with open("portfolio.json", "r") as file:
        portfolio = json.load(file)

    funds_data = []

    total_invested = 0
    total_current_value = 0

    # Fetch NAV for each fund
    for fund in portfolio:
        nav_data = get_nav(fund["scheme_code"])

        current_value = fund["units"] * nav_data["nav"]
        profit = current_value - fund["invested"]
        returns = (profit / fund["invested"]) * 100

        funds_data.append({
            "fund_name": nav_data["fund_name"],
            "scheme_code": nav_data["scheme_code"],
            "nav": nav_data["nav"],
            "date": nav_data["date"],
            "units": fund["units"],
            "invested": fund["invested"],
            "current_value": current_value,
            "profit": profit,
            "returns": returns
        })

        total_invested += fund["invested"]
        total_current_value += current_value

    total_profit = total_current_value - total_invested
    overall_return = (total_profit / total_invested) * 100

    save_history(
    total_current_value,
    total_profit,
    overall_return
)

    report = create_report(
        funds_data,
        total_invested,
        total_current_value,
        total_profit,
        overall_return
    )

    print(report)

    send_email(
        "📊 Daily Mutual Fund Report",
        report
    )


if __name__ == "__main__":
    main()