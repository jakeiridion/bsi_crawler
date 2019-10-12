import requests
from bs4 import BeautifulSoup
import time

article = {}
user_agent = {'User-agent': 'Mozilla/5.0'}
url = "https://www.bsi.bund.de/DE/Themen/ITGrundschutz/ITGrundschutzKompendium/bausteine/SYS/SYS_1_1_Allgemeiner_Server.html;jsessionid=B0793904D3CF0165506E43AFEDBDC3BE.1_cid360"


class CrawledArticle():
    def __init__(self, title, txt):
        self.title = title
        self.txt = txt


class Fetcher():
    def fetch(self):
        time.sleep(1)
        r = requests.get(url, headers=user_agent)
        doc = BeautifulSoup(r.text, "html.parser")


f = Fetcher()
f.fetch()
