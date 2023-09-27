import requests, sys, json

def main():

    try:
        if len(sys.argv) == 1:
            sys.exit("Missing command-line argument")
        elif len(sys.argv) == 2:
            nof_btc = float(sys.argv[1])
        else:
            sys.exit("Please enter only one argument after filename")
    except ValueError:
        sys.exit("Command-line argument is not a number")

    price_btc_USD(nof_btc)

def price_btc_USD(nof_btc):

    count = 0
    while True:
        try:
            data_btc = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            break
        except requests.RequestException:
            if count < 10:
                count += 1
                continue
            else:
                sys.exit("Cannot completed request to fetch data")
    #structured_data = json.dumps(data_btc.json(), indent = 2)

    rate = float(data_btc.json()['bpi']["USD"]["rate"].strip().replace(",",""))

    btc_price = nof_btc * rate

    print(f"${btc_price:,.4f}")


main()