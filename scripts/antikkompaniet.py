import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def antikkompaniet(keyword="teak"):

    base_url="https://www.secondhandbutiken.se/store#/page={}&sort=date&dir=desc&search={}"

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path="/Users/martenvestman/PycharmProjects/teakcurios/driver/chromedriver", options=chrome_options)

    l = []

    for page in range(1, 4, 1):
        #r = requests.get(base_url.format(page, keyword))
        driver.get(base_url.format(page, keyword))

        time.sleep(1)
        #c = r.content
        c = driver.page_source
        soup = BeautifulSoup(c, "html.parser")
        all = soup.find_all("div", {"class": "h24_store_product_list_product"})

        # Selectors
        title = "h24_store_product_list_product_name"
        price = "h24_store_product_list_product_price"

        for item in all:

            d = {}

            try:
                    d["title"] = item.find("div", {"class": title}).text.strip("\n")

            except:
                pass
            try:
                d["price"] = item.find("div", {"class": price}).text.strip("\n\n\t\t\t\t\t\t\t").strip("\t\t\t\t\t\t\n\n\n")
            except:
                pass

            d["site"] = "Antikkompaniet"

            try:
                d["img"] = item.find('img')['src'].replace("?type=gallery_big", "?type=mob_iphone_vi_normal_retina")
            except:
                d["img"] = "static/placeholder-furniture.png"

            try:
                d["url"] = item.find("div", {"class": title}).find('a')['href']
            except:
                pass

            l.append(d)
    l = [dict(t) for t in {tuple(d.items()) for d in l}]
    return l

