from time import sleep

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# 生成随机User-Agent
user_agent = UserAgent()
headers = {'cookie': 'ECC=GoogleBot',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

query = 'Soundcore%20Liberty%204'
pages = 2

# get prods list
prod_ids = []
for page in list(range(1, pages)):
    url = 'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q={}&page={}&sort=sale/dc'.format(
        query, page)
    resp = requests.get(url, headers=headers)
    for prod in resp.json()['prods']:
        prod_ids.append(prod['Id'])
        print('{} - ${}'.format(prod['name'], prod['price']))
    prod_ids = list(set(prod_ids))
    print('There are {} products in list.'.format(len(prod_ids)))