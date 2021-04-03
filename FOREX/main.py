# Importing Libraries

from locale import currency
from forex_python.converter import CurrencyCodes, CurrencyRates
from forex_python.bitcoin import BtcConverter

cur_code = CurrencyCodes() # Creating an instance of Currency Codes
cur_symbol = cur_code.get_symbol('INR') # Fetching Currency Symbol
cur_name = cur_code.get_currency_name('INR') # Fetching Currency Name

# Generating Output

print('Currency Name:', cur_name)
print('Currency Symbol:', cur_symbol)

# Testing Another Currency

print('\n' + cur_code.get_symbol('USD'))
print(cur_code.get_currency_name('USD'))

cur_rate = CurrencyRates() # Generating Currency Rates
rate = cur_rate.get_rate("USD", "INR")

print("1 USD is equal to", rate, "INR")

# Converting USD to INR using Inputs
cur_convtr = cur_rate.convert('USD', 'INR', 25)
print("$" + '25 ' + "is equal to", cur_convtr, "INR")

# BitCoin Converter

print('\nInitiating BTC to INR Rate Exchange')
btc_ini = BtcConverter()

# BTC 2 INR Exchange Rate
btc_INR_ex = btc_ini.get_latest_price('INR')

# BTC 2 INR output
print("1 BTC is equal to", btc_INR_ex)