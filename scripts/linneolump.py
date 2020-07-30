import requests
from bs4 import BeautifulSoup
import unidecode


def linneolump(keyword="teak"):

    base_url="https://linneolump.se/page/{}/?s={}"

    l = []

    for page in range(1, 4, 1):
        r = requests.get(base_url.format(page, keyword))

        print(base_url.format(page,keyword))

        c=r.content
        soup=BeautifulSoup(c,"html.parser")
        all = soup.find("article", {"class":"elementor-post"})

        # Selectors
        title = "element-post__title"
        price = "c-lot-index-lot__estimate-value"

        print(all)

        for item in all:
            d = {}

            try:
                d["title"] = item.find('div', {'class': 'elementor-post__text'}).find("h3", {"class": title}).text
            except:
                pass
            try:
                d["price"] = unidecode.unidecode(item.find("div", {"class": price}).text)
            except:
                pass

            d["site"] = "Linne&Lump"

            try:
                d["img"] = item.find("div", {"class": "elementor-post__thumbnail"}).find("img")["src"]
            except:
                pass

            try:
                d["url"] = item.find('a')['href'].strip()
            except:
                pass

            l.append(d)

        l = [dict(t) for t in {tuple(d.items()) for d in l}]
        return l

for item in linneolump():
    print(item)