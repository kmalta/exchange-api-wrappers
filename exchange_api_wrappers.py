import sys

#Include path for importing
sys.path.append('~/crypto_trading/exchange_api_wrappers')

#Import wrappers
from wrappers.all_wrappers import *

#Imports API Key
from keys.all_keys import *


def main():
    liqui = Liqui(LIQUI_API_KEY, LIQUI_API_SECRET)
    # public api
    liqui.info()
    liqui.ticker('eth_btc')
    liqui.depth('eth_btc')
    liqui.trades('eth_btc')

    # private api
    wallet_info = liqui.balances()
    print(repr(wallet_info))




if __name__ == "__main__":
    main()