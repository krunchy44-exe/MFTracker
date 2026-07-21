import requests


def get_nav(scheme_code):

    url = "https://www.amfiindia.com/spages/NAVAll.txt"

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Unable to download NAV data")

    lines = response.text.split("\n")

    for line in lines:

        data = line.split(";")

        if len(data) < 6:
            continue

        if data[0] == scheme_code:

            return {
                "scheme_code": data[0],
                "fund_name": data[3],
                "nav": float(data[4]),
                "date": data[5]
            }

    raise Exception("Scheme Code not found")