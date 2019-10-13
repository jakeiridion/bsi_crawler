import requests
from bs4 import BeautifulSoup
import time

while True:
    user_agent = {'User-agent': 'Mozilla/5.0'}
    url = input("> ")
    if url == "q":
        break
    print("File is being generated ...")

    time.sleep(1)
    r = requests.get(url, headers=user_agent)
    doc = BeautifulSoup(r.text, "html.parser")


    class Fetcher():
        def get_title(self):
            return doc.select_one(".isFirstInSlot").text

        def fetch(self):
            ges = doc.find_all(["h4", "p", "h2", "li", "h3"])
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

            while True:
                if fin2[0][0:4] != "<h4>":
                    fin2.pop(0)
                else:
                    break
            return fin2

        def write(self):
            fin2 = self.fetch()
            title = self.get_title()
            headerTrue = 0
            test = 0

            with open(str(title) + ".csv", "w") as csv_file:
                for line in fin2:
                    if line[0:4] == "<h3>" or test == 1:
                        headerTrue = 0
                        if test == 1:
                            test = 0
                        else:
                            test = 1

                        continue

                    if line[0:4] == "<h4>":
                        csv_file.write('"' + line.strip("<h4>").strip("</h4>") + '",')
                        prevheader = line
                        headerTrue = 0

                    if line[0:3] == "<p>":
                        if headerTrue == 1:
                            csv_file.write('"' + prevheader.strip("<h4>").strip("</h4>") + '",')
                        csv_file.write('"' + line.strip("<p>").strip("</p>") + '"\n')
                        headerTrue = 1

                    if line[0:4] == "<li>":
                        if headerTrue == 1:
                            csv_file.write('"' + prevheader.strip("<h4>").strip("</h4>") + '",')
                        csv_file.write('"' + line.strip("<li>").strip("</li>") + '"\n')
                        headerTrue = 1


    fetcher = Fetcher()
    fetcher.write()
    print("Done!")
    print(str(fetcher.get_title()) + ".csv has been generated\n")
    input("Press Enter to continue!")