import csv
import sys
import os

csv.field_size_limit(sys.maxsize)


class Extractor():
    name = ""
    links = []

    def __init__(self, filename):
        self.name = filename
        with open(current) as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                self.links.append(row[1])

    def dumpImages(self):
        pass


class ExtractorContainer():
    extractors = {} 

    def add(self, extractor):
        self.extractors.update({extractor.name: extractor})


path = "./CSV"
extractors = ExtractorContainer()
for file in os.listdir(path): 
    current = os.path.join(path, file)
    if os.path.isfile(current):
        extractor = Extractor(current)
        extractors.add(extractor)

for extractor in extractors.extractors.values():
    print(len(extractor.links))

