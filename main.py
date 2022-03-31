import nasdaqdatalink as link
#from initialize import read_key
#from data import get_data

def read_key():
    link.read_key(".key")
    return True

def get_data(ticker):
    data = link.get(ticker)
    return data

def main():
    api_link = read_key()
    if api_link:
        ticker = "NSE/OIL"
        data = get_data(ticker)
        print(data)

if __name__ == "__main__":
    main()
