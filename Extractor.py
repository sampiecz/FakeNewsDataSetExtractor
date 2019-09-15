import csv
import sys
import os
from pathlib import Path
from urllib import request
from bs4 import BeautifulSoup


csv.field_size_limit(sys.maxsize)

class Extractor():
    name = ""
    links = []
    images = {}

    def __init__(self, filename):
        self.name = filename
        with open(current) as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                self.links.append(row[1])
        print("Extractor created.")

    def gatherImgUrls(self):
        for link in self.links:
            try:
                headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
                req = request.Request(link, headers=headers)
                html = request.urlopen(req).read()
                soup = BeautifulSoup(html, "html.parser")
                for img in soup.findAll(itemprop="image"):
                    print("Gathering image urls for link: {}. Source: {}".format(link, img['src']))
                    self.images.update({img['src']: link})
            except Exception as e:
                print("Bad link: {}".format(link))


    def dumpImages(self):

        path = Path().absolute()

        count = 0

        for img_src, page_link in self.images.items():

            first_half = page_link.split("//")[1]
            domain = first_half.split(".")[0]

            folder_path = str(path)+ "/img/{}/{}".format(self.name, domain)
            os.makedirs(folder_path)
            image_path = folder_path + "/{}.jpg".format(str(count))
            print("Dumping img: {}".format(url))
            request.urlretrieve(url, image_path)
            count += 1


class ExtractorContainer():
    extractors = {} 

    def add(self, extractor):
        self.extractors.update({extractor.name: extractor})


# Generate extractors, and extractor container
path = "./CSV"
container  = ExtractorContainer()
for file in os.listdir(path): 
    current = os.path.join(path, file)
    if os.path.isfile(current):
        extractor = Extractor(current)
        container.add(extractor)

for extractor in container.extractors.values():
    extractor.gatherImgUrls()
    extractor.dumpImages()
