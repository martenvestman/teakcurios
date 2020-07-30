import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def blocket(keyword="teak"):

    base_url="https://www.blocket.se/annonser/hela_sverige/for_hemmet/mobler_heminredning?cg=2040&page={}&q={}"

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path="/Users/martenvestman/PycharmProjects/teakcurios/driver/chromedriver", options=chrome_options)

    l = []

    for page in range(1, 4, 1):
        driver.get(base_url.format(page, keyword))
        y = 400
        for timer in range(0, 8):
            driver.execute_script("window.scrollTo(0, " + str(y) + ")")
            y += 1000
            time.sleep(1)
        c = driver.page_source
        soup = BeautifulSoup(c, "html.parser")

        all = soup.find_all("div", {"class": "itHtzm"})

        # Selectors
        title = "eNJmTh"
        price = "bNwNaE"

        for item in all:

            d = {}

            try:
                d["title"] = item.find("span", {"class": title}).text
            except:
                pass
            try:
                d["price"] = item.find("div", {"class": price}).text
            except:
                pass

            d["site"] = "Blocket"

            try:
                d["img"] = item.find('img')['src'].replace("?type=gallery_big", "?type=mob_iphone_vi_normal_retina")
            except:
                d["img"] = "static/placeholder-furniture.png"

            try:
                d["url"] = "https://www.blocket.se" + item.find('h2', {'class': 'bcaUdR'}).find('a')['href'].strip().replace(" ","%20")
            except:
                pass

            l.append(d)
    l = [dict(t) for t in {tuple(d.items()) for d in l}]
    return l

