import requests
from bs4 import BeautifulSoup
import time

article = {}
user_agent = {'User-agent': 'Mozilla/5.0'}
url = "https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzKompendium/bausteine/SYS/SYS_4_1_Drucker,_Kopierer_und_Multifunktionsger%C3%A4te.html"


class CrawledArticle():
    def __init__(self, title, txt):
        self.title = title
        self.txt = txt


class Fetcher():
    def fetch(self):
        time.sleep(1)
        r = requests.get(url, headers=user_agent)
        doc = BeautifulSoup(r.text, "html.parser")

        ges = doc.find_all(["h4", "p", "h2", "li"])  # ,li für listen
        fin = []
        fin2 = []

        for i in ges:
            if "navToTop" in str(i) or "class=" in str(i) or "a href" in str(i):
                continue

            fin.append(str(i))

        o = 0
        for i in fin:
            if (i[0:3] == "<p>" or i[0:4] == "<h2>") and o == 0:
                continue

            if i[0:4] == "<h4>":
                o = 1

            fin2.append(i)

        # make all the useless stuff pop

        for i in fin2:
            print(i)


f = Fetcher()
f.fetch()
