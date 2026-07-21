from jinja2 import Environment, FileSystemLoader


def create_report(fund_name, scheme_code, nav, date, units, invested):
    current_value = units * nav
    profit = current_value - invested
    returns = (profit / invested) * 100

    profit_class = "green" if profit >= 0 else "red"

    

    env = Environment(loader=FileSystemLoader("templates"))

    template = env.get_template("report.html")

    html = template.render(
        fund_name=fund_name,
        scheme_code=scheme_code,
        nav=nav,
        date=date,
        units=units,
        invested=f"{invested:,.2f}",
        current_value=f"{current_value:,.2f}",
        profit=f"{profit:,.2f}",
        returns=f"{returns:.2f}",
        profit_class=profit_class
    )

    return html