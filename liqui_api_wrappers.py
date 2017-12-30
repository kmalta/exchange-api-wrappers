import requests
import json

#Imports API Key
from keys.liqui_api_key import *

base_url = 'https://api.liqui.io/api/3'

#Status Code Error Handling
def status_check(response):
    if response.status_code == 200:
        return reponse.json()
    else:
        response.raise_for_status()

def create_url(*args):
    return '/'.join(base_url, *args)

#Get info from all coins
def get_info_all():
    url = create_url('info')
    response = requests.get(url)
    return status_check(response)

#Get info from pair
def get_info_pairs(from_coin, to_coin):
    response = get_info_all()
    return response['pairs'][from_coin + '_' to_coin]

#Get daily stats between trades from one coin to another
def get_ticker(from_coin, to_coin):
    url = create_url('ticker', from_coin + '_' + to_coin)
    response = requests.get(url)
    return status_check(response)

def get_depth(from_coin, to_coin):
    url = create_url('depth', from_coin + '_' + to_coin)
    response = requests.get(url)
    return status_check(response)


def get_trades(from_coin, to_coin):
    url = create_url('trades', from_coin + '_' + to_coin)
    response = requests.get(url)
    return status_check(response)
