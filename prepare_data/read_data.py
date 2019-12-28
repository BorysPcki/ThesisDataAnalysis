import csv


class ProcessedData:
    x = []
    y = []

    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path) as fileCSV:
            reader_csv = csv.reader(fileCSV)
            for row in reader_csv:
                self.x.append(round(float(row[0]), 5))
                self.y.append(round(float(row[1]), 7))
