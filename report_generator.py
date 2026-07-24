def create_report(funds_data, total_invested, total_current_value, total_profit, overall_return):

    rows = ""

    for fund in funds_data:
        color = "green" if fund["profit"] >= 0 else "red"

        rows += f"""
        <tr>
            <td>{fund['fund_name']}</td>
            <td>₹{fund['nav']:.2f}</td>
            <td>{fund['units']:.3f}</td>
            <td>₹{fund['invested']:,.2f}</td>
            <td>₹{fund['current_value']:,.2f}</td>
            <td style="color:{color};">₹{fund['profit']:,.2f}</td>
            <td style="color:{color};">{fund['returns']:.2f}%</td>
        </tr>
        """

    total_color = "green" if total_profit >= 0 else "red"

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f4f4f4;
                padding: 20px;
            }}

            .container {{
                max-width: 1100px;
                margin: auto;
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,.1);
            }}

            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }}

            th {{
                background: #2c3e50;
                color: white;
                padding: 10px;
            }}

            td {{
                border: 1px solid #ddd;
                padding: 10px;
                text-align: center;
            }}

            .summary {{
                margin-top: 30px;
                background: #f8f9fa;
                padding: 20px;
                border-radius: 8px;
            }}

            .summary p {{
                font-size: 16px;
                margin: 8px 0;
            }}
        </style>
    </head>

    <body>

    <div class="container">

        <h2 align="center">📊 Daily Mutual Fund Report</h2>

        <table>

            <tr>
                <th>Fund</th>
                <th>NAV</th>
                <th>Units</th>
                <th>Invested</th>
                <th>Current Value</th>
                <th>Profit/Loss</th>
                <th>Returns</th>
            </tr>

            {rows}

        </table>

        <div class="summary">

            <h3>💼 Portfolio Summary</h3>

            <p><b>Total Invested:</b> ₹{total_invested:,.2f}</p>

            <p><b>Current Value:</b> ₹{total_current_value:,.2f}</p>

            <p style="color:{total_color};">
                <b>Total Profit/Loss:</b> ₹{total_profit:,.2f}
            </p>

            <p style="color:{total_color};">
                <b>Overall Return:</b> {overall_return:.2f}%
            </p>

        </div>

    </div>

    </body>
    </html>
    """

    return html