import requests
import json

def get_exchange_rates():
    api_key = "5f0e46c1b217137e3d282279"  # Replace with your Open Exchange Rates API key
    base_url = f"https://open.er-api.com/v6/latest/INR?apikey=5f0e46c1b217137e3d282279"
    
    try:
        response = requests.get(base_url)
        
        if response.status_code != 200:
            raise ValueError(f"Error: API request failed with status code {response.status_code}")

        data = response.json()

        if "rates" not in data:
            raise ValueError("Error: 'rates' not found in API response.")

        return data["rates"]
    
    except json.JSONDecodeError as e:
        raise ValueError(f"Error: Unable to parse JSON response: {e}")
    except Exception as e:
        raise ValueError(f"Error: {e}")

def main():
    print("Currency Converter and Price Comparison")

    exchange_rates = get_exchange_rates()
    
    # Dictionary mapping currency codes to symbols
    currency_symbols = {
    "AED": "د.إ",   "AFN": "؋",     "ALL": "L",      "AMD": "֏",     "ANG": "ƒ","AOA": "Kz",    "ARS": "$",     "AUD": "$",     "AWG": "ƒ",     "AZN": "₼",
"BAM": "KM",    "BBD": "$",     "BDT": "৳",     "BGN": "лв",    "BHD": ".د.ب","BIF": "FBu",   "BMD": "$",     "BND": "$",     "BOB": "Bs.",   "BRL": "R$",
"BSD": "$",     "BTN": "Nu.",   "BWP": "P",      "BYN": "Br",    "BZD": "BZ$","CAD": "$",     "CDF": "FC",    "CHF": "CHF",    "CLP": "$",     "CNY": "¥",
"COP": "$",     "CRC": "₡",     "CUP": "$",     "CVE": "$",     "CZK": "Kč","DJF": "Fdj",   "DKK": "kr",    "DOP": "RD$",   "DZD": "د.ج",   "EGP": "£",
"ERN": "Nfk",   "ETB": "Br",    "EUR": "€",     "FJD": "$",     "FKP": "£","FOK": "kr",    "GBP": "£",     "GEL": "₾",     "GGP": "£",     "GHS": "₵",
"GIP": "£",     "GMD": "D",     "GNF": "FG",    "GTQ": "Q",     "GYD": "$","HKD": "$",     "HNL": "L",     "HRK": "kn",    "HTG": "G",     "HUF": "Ft",
"IDR": "Rp",    "ILS": "₪",     "IMP": "£",     "INR": "₹",     "IQD": "ع.د",
"IRR": "﷼",    "ISK": "kr",    "JEP": "£",     "JMD": "J$","JPY": "¥",     "KES": "Ksh",   "KGS": "сом",   "KHR": "៛",    "KID": "$",
"KIN": "₭",     "KRW": "₩",    "KWD": "د.ك",   "KYD": "$",    "KZT": "₸","LAK": "₭",     "LBP": "ل.ل",   "LKR": "₨",     "LRD": "$",    "LSL": "L",
"LYD": "ل.د",   "MAD": "د.م.",  "MDL": "L",     "MGA": "Ar",    "MKD": "ден","MMK": "Ks",    "MNT": "₮",    "MOP": "P",     "MRU": "UM",    "MUR": "₨",
"MVR": "Rf",    "MWK": "MK",   "MXN": "$",     "MYR": "RM",    "MZN": "MT","NAD": "$",     "NGN": "₦",    "NIO": "C$",    "NOK": "kr",    "NPR": "₨",
"NZD": "$",     "OMR": "﷼",   "PAB": "B/.",    "PEN": "S/.",   "PGK": "K","PHP": "₱",     "PKR": "₨",    "PLN": "zł",    "PYG": "₲",     "QAR": "﷼",
"RON": "lei",   "RSD": "дин.",  "RUB": "₽",     "RWF": "FRw",   "SAR": "﷼","SBD": "$",     "SCR": "₨",    "SDG": "ج.س.",  "SEK": "kr",    "SGD": "$",
"SHP": "£",     "SLL": "Le",   "SOS": "Sh",    "SRD": "$",     "SSP": "£","STN": "Db",    "SYP": "£",    "SZL": "L",     "THB": "฿",
"TMT": "T",     "TND": "د.ت",  "TOP": "T$",    "TRY": "₺",     "TTD": "TT$","TVD": "$",     "TWD": "NT$",  "TZS": "TSh",   "UAH": "₴",     "UGX": "USh",
"USD": "$",     "UYU": "$U",   "VES": "Bs",    "VND": "₫",     "VUV": "VT", "WST": "T",     "XAF": "FCFA", "XCD": "$",    "XDR": "SDR",    "XOF": "CFA",
"XPF": "₣",     "YER": "﷼",   "ZAR": "R",     "ZMW": "ZK",    "ZWL": "Z$",

}


    supported_currencies = exchange_rates.keys()

    while True:
        try:
            amount = float(input("Enter the amount: "))
            from_currency = input("Enter the source currency code (e.g., USD):").upper()

            print("Select a target currency:")
            to_currency = input("Enter the target currency code: ").upper()

            if from_currency == to_currency:
                print("Source and target currencies are the same. Please enter different currencies.")
                continue

            if from_currency not in supported_currencies or to_currency not in supported_currencies:
                raise ValueError("Invalid currency codes.")

            exchange_rate = exchange_rates[to_currency] / exchange_rates[from_currency]
            result = amount * exchange_rate

            from_symbol = currency_symbols.get(from_currency, from_currency)
            to_symbol = currency_symbols.get(to_currency, to_currency)

            print(f"{amount} {from_symbol} is equal to {result:.2f} {to_symbol}")

        except ValueError as e:
            print(f"Error: {e}")
            continue

        another_conversion = input("Do you want to perform another conversion? (yes/no): ").lower()
        if another_conversion != 'yes':
            break

if __name__ == "__main__":
    main()
