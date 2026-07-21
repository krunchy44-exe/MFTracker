import json

from nav_fetcher import get_nav
from report_generator import create_report
from email_sender import send_email


def main():
    # Load portfolio
    with open("portfolio.json", "r") as file:
        portfolio = json.load(file)

    # Fetch latest NAV
    fund = get_nav(portfolio["scheme_code"])

    # Generate report
    report = create_report(
        fund["fund_name"],
        fund["scheme_code"],
        fund["nav"],
        fund["date"],
        portfolio["units"],
        portfolio["invested"]
    )

    # Display report
    print(report)
    
    send_email(
    "📊 Daily Mutual Fund Report",
    report
)





















if __name__ == "__main__":
    main()