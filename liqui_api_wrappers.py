from wrappers.base_api_wrapper_class import *

class LiquiAPIError(APIError):
    pass

class Liqui(APIWrapper):
    def __init__(self, key, secret):
        base_url = 'https://api.liqui.io'
        get = 'api/3'
        post = 'tapi'
        super().__init__(key, secret, base_url, get, post)


    ###########################################
    #######     OVERRIDDEN FUNCTIONS    #######
    ###########################################

    def _raise_error(self, err):
        return LiquiAPIError(err)

    def _trade_request(self, **params):
        if not self._key or not self._secret:
            self._raise_error('Issue with API Keys.')
        params.update(nonce=int(time()))
        headers = self.__create_headers(params)
        response = requests.post(self._make_url(self.post), data=params, headers=headers)
        return self._check_success(response)


    ###########################################
    ##########       PUBLIC API      ##########
    ###########################################

    #Get info from all coins
    def info(self):
        return self._get_request('info')

    #Get info from pair
    def info_pairs(self, pair):
        return self.info()['pairs'][pair]

    #Get daily stats between trades from one coin to another
    def ticker(self, pair):
        return self._get_request('ticker', pair)

    def depth(self, pair):
        return self._get_request('depth', pair)

    def trades(self, pair):
        return self._get_request('trades', pair)


    ###########################################
    ##########      PRIVATE API      ##########
    ###########################################

    def __create_headers(self, params):
        from collections import defaultdict
        header_params = defaultdict()
        header_params['Key'] = self._key
        header_params['Sign'] = self._sign(params)
        return header_params

    def get_info(self):
        return self._trade_request(method='getInfo')

    def balances(self):
        funds = self.get_info()['return']['funds']
        return {currency: balance for currency, balance in funds.items() if balance != 0}

    def active_orders(self, pair=''):
        return self._trade_request(method='ActiveOrders', pair=pair)

    def order_info(self, order_id):
        return self._trade_request(method='OrderInfo', order_id=order_id)

    def cancel_order(self, order_id):
        return self._trade_request(method='CancelOrder', order_id=order_id)

    def trade_history(self, **params):
        return self._trade_request(method='TradeHistory', **params)

    def trade(self, pair, type, rate, amount):
        return self._trade_request(method='Trade', pair=pair, type=type, rate=rate, amount=amount)

    def buy(self, pair, rate, amount):
        return self.trade(pair, 'buy', rate, amount)

    def sell(self, pair, rate, amount):
        return self.trade(pair, 'sell', rate, amount)


