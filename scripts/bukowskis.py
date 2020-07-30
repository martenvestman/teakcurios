import requests
from bs4 import BeautifulSoup
import unidecode


def bukowskis(keyword="teak"):

    base_url="https://www.bukowskis.com/sv/lots/page/{}/search/{}"

    l = []

    for page in range(1, 4, 1):
        r = requests.get(base_url.format(page, keyword))


        c=r.content
        soup=BeautifulSoup(c,"html.parser")
        all = soup.find("div", {"class":"c-lot-index-lots"})

        # Selectors
        title = "c-lot-index-lot__title"
        price = "c-lot-index-lot__estimate-value"

        for item in all:

            d = {}

            try:
                d["title"] = item.find("a", {"class": title}).text
            except:
                pass
            try:
                d["price"] = unidecode.unidecode(item.find("div", {"class": price}).text)
            except:
                pass

            d["site"] = "Bukowskis"

            try:
                d["img"] = item.find('img')['data-original']
            except:
                d["img"] = item.find('img')['src']

            try:
                d["url"] = "https://www.bukowskis.com/" + item.find('a')['href'].strip()
            except:
                pass

            l.append(d)

        l = [dict(t) for t in {tuple(d.items()) for d in l}]
        return l

