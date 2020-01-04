import csv
import re


class Data:
    x = []
    y = []

    def __init__(self, path):
        self.path = path

    @staticmethod
    def read_data(path):
        with open(path) as fileCSV:
            reader_csv = csv.reader(fileCSV, delimiter='\t')
            rows = [row for row in reader_csv]
        return rows

    @staticmethod
    def process_data(rows):
        zero = 0
        for i in range(len(rows)):
            if rows[i]:
                if rows[i][0]:
                    if re.search(":", rows[i][0]):
                        if re.search(":", rows[i][0]).end():
                            hours = rows[i][0][re.search(":", rows[i][0]).end() - 3:re.search(":", rows[i][0]).end()-1]
                            minutes = rows[i][0][re.search(":", rows[i][0]).end():re.search(":", rows[i][0]).end()+2]
                            rows[i][0] = rows[i][0][re.search(":", rows[i][0]).end() + 3:]
                            rows[i][0] = rows[i][0]
                            rows[i][0] = rows[i][0].replace(',', '.')
                            rows[i][0] = float(rows[i][0]) + int(hours)*60*60 + int(minutes)*60
                            if not zero:
                                zero = float(rows[i][0])
                            rows[i][0] = round(rows[i][0] - zero, 5)

                if rows[i][1]:
                    if re.search("E", rows[i][1]):
                        exponent_index = re.search("E", rows[i][1]).start()
                        exponent = rows[i][1][exponent_index + 1:]
                        if exponent[0] == '-':
                            exponent = -1 * int(exponent[1:])
                        else:
                            exponent = int(exponent)
                        rows[i][1] = rows[i][1].replace(',', '.')
                        rows[i][1] = round(float(rows[i][1][:exponent_index]) * (10 ** exponent), 7)
        return rows

    def display_data(self, number_of_rows):
        rows = self.process_data(self.read_data(self.path))
        for i in range(number_of_rows):
            print(rows[i])
        print()

    def append_data(self):
        rows = self.process_data(self.read_data(self.path))
        for row in rows:
            if row:
                if row[0] or row[0] == 0:
                    if isinstance(row[0], float):
                        self.x.append(row[0])
                if row[1] or row[1] == 0:
                    if isinstance(row[1], float):
                        self.y.append(row[1])

    def return_data(self):
        self.append_data()
        value = [self.x, self.y]
        return value

    def clear_data(self):
        self.x.clear()
        self.y.clear()
