import requests
from bs4 import BeautifulSoup
import time

user_agent = {'User-agent': 'Mozilla/5.0'}
url = "https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzKompendium/bausteine/SYS/SYS_3_1_Laptops.html"

time.sleep(1)
r = requests.get(url, headers=user_agent)
doc = BeautifulSoup(r.text, "html.parser")


class Fetcher():
    def get_title(self):
        return doc.select_one(".isFirstInSlot").text

    def fetch(self):
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
        while True:
            if fin2[-1][0:5] != "<h2>4":
                fin2.pop()

            else:
                fin2.pop()
                break

        return fin2

    def write(self):
        fin2 = self.fetch()
        print(fin2)

    
fetcher = Fetcher()
title = fetcher.get_title()
fetcher.write()