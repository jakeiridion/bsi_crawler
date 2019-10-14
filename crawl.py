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
            firsth = 0
            samelist = 0

            with open(str(title) + ".csv", "w") as csv_file:
                for line in fin2:

                    # Header <h3> / <h4>

                    if line[0:4] == "<h3>" or test == 1:
                        headerTrue = 0
                        if test == 1:
                            test = 0
                        else:
                            test = 1

                        continue

                    if line[0:4] == "<h4>":
                        if firsth == 0:
                            firsth = 1
                        else:
                            csv_file.write("\n\n")

                        splited = line.strip("<h4>").strip("</h4>").strip().split(" ")
                        s_number = splited[0]
                        s_title = " ".join(splited[1:])

                        prevnumber = s_number
                        prevtitle = s_title
                        headerTrue = 0

                    # Paragraphen <p>

                    if line[0:3] == "<p>":
                        sentences = line.strip("<p>").strip("</p>").strip().split(".")

                        if headerTrue == 1:
                            csv_file.write("\n")

                        for sentenc in sentences[:-1]:
                            csv_file.write('"' + prevnumber + '","' + prevtitle + '","' + sentenc.strip() + '."\n')

                        headerTrue = 1

                    # Listen <li>

                    if line[0:4] == "<li>":
                        if samelist == 0:
                            csv_file.write("\n")

                        if headerTrue == 1:
                            samelist = 1

                        sentences = line.strip("<li>").strip("</li>").strip()
                        csv_file.write('"' + prevnumber + '","' + prevtitle + '","' + sentences + '"\n')

                        headerTrue = 1


    fetcher = Fetcher()
    fetcher.write()
    print("Done!")
    print(str(fetcher.get_title()) + ".csv has been generated\n")