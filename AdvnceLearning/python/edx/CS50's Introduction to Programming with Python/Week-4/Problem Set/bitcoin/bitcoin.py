import sys
import requests

def get_bitcoin_price():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()  # Raise an exception for 4XX or 5XX status codes
        data = response.json()
        return float(data['bpi']['USD']['rate_float'])
    except requests.RequestException as e:
        print(f"Error fetching Bitcoin price: {e}")
        sys.exit(1)

def main():
    # Check if the number of command-line arguments is correct
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)

    # Try to convert the command-line argument to a float
    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

    bitcoin_price = get_bitcoin_price()
    cost_in_usd = bitcoins * bitcoin_price
    print(f"The cost of {bitcoins:,.4f} Bitcoins is ${cost_in_usd:,.4f}")

if __name__ == "__main__":
    main()
