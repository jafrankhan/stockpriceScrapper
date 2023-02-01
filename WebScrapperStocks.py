# Created by Mohamed Jafaran Khan
# This is Web Scraping Project to scrap stock price
import pandas as pd
import datetime
import bs4
import requests
from bs4 import BeautifulSoup

# web scrapping: getting of the data

def getData(symbol):
    url = f"https://sg.finance.yahoo.com/quote/{symbol}"
    r  = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    soup = bs4.BeautifulSoup(r.text,"html.parser")

    stock = {
    symbol : symbol,
    "price" : soup.find("div", {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text
    #"change" : soup.find("div", {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text,
    #"percent" :soup.find("div", {'class':'D(ib) Mend(20px)'}).find_all('fin-streamer')[2].text,
    
    }

    if stock == []:
        stock = "99999"

    return stock

HSI = ["S51.SI","TSLA","AAPL","GOOGL"]

for step in range(1,101):
    price2 = []
    col2 = []
    timestamp = datetime.datetime.now()
    timestamp = timestamp.strftime("%m/%d/%Y, %H:%M:%S")
    for stockcode in HSI:
       price2.append(getData(stockcode)["price"])
    col = [timestamp]
    col.extend(price2)
    df = pd.DataFrame(col)
    df = df.T
    df.to_csv("Realtime stock data.csv",mode = "a", header = False)
    print(col)


    




