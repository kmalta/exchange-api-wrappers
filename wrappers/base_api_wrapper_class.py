import requests
import json
import hmac
import hashlib
from time import time

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode



class APIError(Exception):
    pass

class APIWrapper(object):
    def __init__(self, key, secret, base_url, get, post):
        self.base_url = base_url
        self.get = get
        self.post = post
        self._secret = secret
        self._key = key
    def _status_check(self, response):
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
    def _check_success(self, response):
        json = self._status_check(response)
        if json['success'] == 1:
            return json
        else:
            self._raise_error('Unsuccessful request.')
    def _raise_error(self, err):
        return APIError(err)
    def _make_url(self, ext, *args):
        return '/'.join([self.base_url, ext] + list(args))
    def _get_request(self, *args):
        url = self._make_url(self.get, *args)
        response = requests.get(url)
        return self._status_check(response)
    def _trade_request(self, **params):
        pass
    def _sign(self, data):
        if isinstance(data, dict):
            data = urlencode(data)
        return hmac.new(self._secret.encode(), data.encode(), hashlib.sha512).hexdigest()

