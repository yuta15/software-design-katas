import json
import csv

from application import OutputterPort
from .formatter import JsonDataFormatter, TSVDataFormatter, CSVDataFormatter


class JsonOutputter(OutputterPort):
    def __init__(self, formatter:JsonDataFormatter):
        super().__init__(formatter)

    def output(self):
        formatted_data = self._formatter.format()
        with open("./output.json", mode="w") as f:
            json.dump(formatted_data.data, f, indent=4)


class TsvOutputter(OutputterPort):
    def __init__(self, formatter:TSVDataFormatter):
        super().__init__(formatter)

    def output(self):
        formatted_data = self._formatter.format()
        with open("./output.tsv", mode="w") as f:
            for d in formatted_data.data:
                f.writelines(f"{d}\n")


class CsvOutputter(OutputterPort):
    def __init__(self, formatter:CSVDataFormatter):
        super().__init__(formatter)

    def output(self):
        formatted_data = self._formatter.format()
        with open("./output.csv", mode="w") as f:
            writer = csv.writer(f)
            writer.writerows(formatted_data.data)