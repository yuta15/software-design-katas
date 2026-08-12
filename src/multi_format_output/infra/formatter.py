from dataclasses import asdict

from application import FormatterPort

from .models import CSVFormat, JsonFormat, TSVFormat


class CSVDataFormatter(FormatterPort):
    def __init__(self, data):
        super().__init__(data)

    def format(self) -> CSVFormat:
        dict_data = asdict(self.data)
        headers = []
        values = []
        for key, value in dict_data.items():
            str_key = str(key)
            str_value = str(value)
            headers.append(str_key)
            values.append(str_value)
        return CSVFormat([headers, values])


class JsonDataFormatter(FormatterPort):
    def __init__(self, data):
        super().__init__(data)

    def format(self) -> JsonFormat:
        dict_data = asdict(self.data)
        normalized_item = {}
        for key, value in dict_data.items():
            if isinstance(value, int):
                normalized_item[key] = value
            else:
                normalized_item[key] = str(value)
        return JsonFormat(data=normalized_item)


class TSVDataFormatter(FormatterPort):
    def __init__(self, data):
        super().__init__(data)

    def format(self) -> TSVFormat:
        dict_data = asdict(self.data)
        headers = "\t".join(str(key) for key in dict_data)
        values = "\t".join(str(value) for value in dict_data.values())
        return TSVFormat(data=[headers, values])
