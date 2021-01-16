# coding=utf-8
from http import cookies
import json
import requests
import random
from fake_useragent import UserAgent
from http.cookies import SimpleCookie

# 自动 userAgent
ua = UserAgent()

with open('./mobile_user_agents.txt') as f:
    # for i in f.readlines():
    #     print(i.strip())
    mobile_user_agents = [i.strip() for i in f.readlines()]
    
def get_ua(is_mobile = False):
    return random.choice(mobile_user_agents) if is_mobile else ua.random

# 手动 userAgent
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}

# 解析 cookies
def get_cookie():
    ck = SimpleCookie()
    with open("./cookie.txt") as f:
        ck.load((f.read()))

    cookies = {}
    for key, morsel in ck.items():
        cookies[key] = morsel.value
    return cookies


# 调用代理池
def get_proxy():
    pass


url = """https://h5api.m.taobao.com/h5/mtop.taobao.maserati.personal.works/1.0/?jsv=2.6.1&appKey=12574478&t=1610787029456&sign=52ff50dbf8f11b7771a2275dfd88c43a&v=1.0&api=mtop.taobao.maserati.personal.works&preventFallback=true&type=jsonp&dataType=jsonp&callback=mtopjsonp6&data=%7B%22source%22%3A%22normal%22%2C%22type%22%3A%22h5%22%2C%22userId%22%3A%222830069487%22%2C%22page%22%3A5%2C%22sort%22%3A%22default%22%2C%22sortType%22%3A0%7D"""

# 获取网页
def get_content(url):
    cookies = get_cookie()
    r = requests.get(url, headers = headers, cookies = cookies)
    return r.content

text = get_content(url)

# 解析网页
def parse_content(text):
    text = text[12:-1]
    rv = json.loads(text)
    containList = rv['data']['result']['data']['feeds']
    for list in containList:
        downList = list.values()[0]
        if (downList.startswith('https')):
            print(downList)
        else:
            pass
        
# parse_content(text)
