import requests
from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import time
import unidecode


def lauritz(keyword="teak"):

    base_url="https://www.lauritz.com/sv/auktioner/?FLId=3&FText=teak&OD=False"
    dynamic_url="https://www.lauritz.com/sv/auktioner/?FLId=3&FText={}&OD=False".format(keyword)


    if keyword:
        r = requests.get(dynamic_url)
    else:
        r = requests.get(base_url)

    c = r.content

    soup = BeautifulSoup(c, "html.parser")

    all = soup.find_all("table", {"class": "ADListNoHighLight"})

    l = []


    # Selectors
    title = "pListLinkHeader"
    price = "valuation"

    for page in range(0, 1, 1):
        r = requests.get(base_url)
        c = r.content

        for item in all:

            d = {}

            try:
                d["title"] = item.find("span", {"class": title}).text.replace("\n", "")
            except:
                pass
            try:
                d["price"] = unidecode.unidecode(item.find("td", {"class": price}).text.replace("\n", ""))
            except:
                pass

            d["site"] = "Lauritz"

            try:
                d["img"] = item.find("div", {"class": "ListLotImage"}).find('input')['src'].replace("?width=200","")
            except:
                d["img"] = "static/placeholder-furniture.png"

            try:
                d["url"] = "https://www.lauritz.com" + item.find('span', {'class': title}).find('a')['href'].strip().replace(" ","%20")
            except:
                pass

            l.append(d)

    return l




