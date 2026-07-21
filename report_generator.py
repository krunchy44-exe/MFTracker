def create_report(fund_name, scheme_code, nav, date, units, invested):
    current_value = units * nav
    profit = current_value - invested
    returns = (profit / invested) * 100

    profit_color = "green" if profit >= 0 else "red"

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                padding: 20px;
            }}
            .container {{
                background: white;
                padding: 20px;
                border-radius: 10px;
                max-width: 600px;
                margin: auto;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
            }}
            td {{
                padding: 10px;
                border-bottom: 1px solid #ddd;
            }}
            .profit {{
                color: {profit_color};
                font-weight: bold;
            }}
        </style>
    </head>

    <body>
        <div class="container">
            <h2>📊 Daily Mutual Fund Report</h2>

            <table>
                <tr>
                    <td><b>Fund Name</b></td>
                    <td>{fund_name}</td>
                </tr>

                <tr>
                    <td><b>Scheme Code</b></td>
                    <td>{scheme_code}</td>
                </tr>

                <tr>
                    <td><b>NAV</b></td>
                    <td>₹{nav:.2f}</td>
                </tr>

                <tr>
                    <td><b>Date</b></td>
                    <td>{date}</td>
                </tr>

                <tr>
                    <td><b>Units</b></td>
                    <td>{units:.3f}</td>
                </tr>

                <tr>
                    <td><b>Invested</b></td>
                    <td>₹{invested:,.2f}</td>
                </tr>

                <tr>
                    <td><b>Current Value</b></td>
                    <td>₹{current_value:,.2f}</td>
                </tr>

                <tr>
                    <td><b>Profit/Loss</b></td>
                    <td class="profit">₹{profit:,.2f}</td>
                </tr>

                <tr>
                    <td><b>Returns</b></td>
                    <td class="profit">{returns:.2f}%</td>
                </tr>
            </table>
        </div>
    </body>
    </html>
    """

    return html