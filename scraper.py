import urllib.request
import ssl
import os
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        ssl._create_default_https_context = ssl._create_unverified_context
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        counter = 0
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "articles" in url:
                print("¥n" + url)
                newsData = urllib.request.urlopen(self.site + url)
                newsHtml = newsData.read().decode('utf-8')
                htmlPath = os.path.join("/Users", "sakinamae", "PycharmProjects", str(counter) + ".html")
                htmlFile = open(htmlPath, "w", encoding="utf-8")
                htmlFile.write(newsHtml)
                htmlFile.close()
                counter += 1
            if counter >= 10:
                break


news = "https://news.google.com/"
Scraper(news).scrape()
