import requests

API_KEY = "66bb184ea983a8a634dce57a59ff898f"
BASE_URL = "http://data.fixer.io/api/latest"

def convert(amount, from_currency, to_currency):
    params = {

        
        "access_key": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if "error" in data:
        print(f"Error: {data['error']}")
        return None

    rates = data["rates"]

    if from_currency not in rates or to_currency not in rates:
        print("Currency not found!")
        return None

    # Convert via EUR base
    eur_amount = amount / rates[from_currency]
    converted_amount = eur_amount * rates[to_currency]
    return converted_amount

amount = float(input("Enter amount: "))
from_currency = input("From currency (e.g., USD): ").upper()
to_currency = input("To currency (e.g., INR): ").upper()

result = convert(amount, from_currency, to_currency)
if result:
    print(f"{amount} {from_currency} = {result:.2f} {to_currency}")
