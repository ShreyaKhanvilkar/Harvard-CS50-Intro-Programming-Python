import requests
import sys


def main():
    check_exceptions()
    print(price())


def check_exceptions():
    if len(sys.argv) == 2:
        if not float(sys.argv[1]):
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Missing command-line argument")


def price():
    try:
        request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response = request.json()
        cost = response["bpi"]["USD"]["rate_float"] * float(sys.argv[1])
        return f"${cost:,.4f}"
    except requests.RequestException:
        return None


main()
