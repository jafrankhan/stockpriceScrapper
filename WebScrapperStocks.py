# Created by Mohamed Jafaran Khan
# This is Web Scraping Project to scrap stock price

import bs4
import requests
from bs4 import BeautifulSoup


def getData(symbol):
    url = f"https://sg.finance.yahoo.com/quote/{symbol}"
    r  = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = bs4.BeautifulSoup(r.text,"html.parser")

    stock = {
    symbol : symbol,
    "price" : soup.find("div", {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text,
    "change" : soup.find("div", {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text,
    "percent" :soup.find("div", {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[2].text
    }
    return stock


print(getData("VAST.L"))

