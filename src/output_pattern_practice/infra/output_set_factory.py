from dataclasses import dataclass

from domain import Data
from application import DataFormatType, OutputSetFactory, OutputterPort, FormatterPort


@dataclass
class OutputSetDependencies:
    json_formatter:type[FormatterPort]
    csv_formatter:type[FormatterPort]
    tsv_formatter:type[FormatterPort]
    json_outputter:type[OutputterPort]
    csv_outputter:type[OutputterPort]
    tsv_outputter:type[OutputterPort]


class ImpleOutputSetFactory(OutputSetFactory):
    def __init__(self, dependencies:OutputSetDependencies):
        self._dependencies = dependencies

    def create(self, format_type: DataFormatType, data:Data) -> OutputterPort:
        if format_type == DataFormatType.JSON:
            return self._dependencies.json_outputter(formatter=self._dependencies.json_formatter(data=data))
        elif format_type == DataFormatType.CSV:
            return self._dependencies.csv_outputter(formatter=self._dependencies.csv_formatter(data=data))
        elif format_type == DataFormatType.TSV:
            return self._dependencies.tsv_outputter(formatter=self._dependencies.tsv_formatter(data=data))
        raise ValueError("Invalid value")