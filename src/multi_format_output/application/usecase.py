from dataclasses import dataclass

from domain import NewEntityFactory

from .models import DataFormatType
from .port import OutputSetFactory


@dataclass
class Input:
    data: dict
    output_type: str = "JSON"


class Usecase:
    def __init__(self, output_set_factory: OutputSetFactory, new_entity_factory: NewEntityFactory):
        self._output_set_factory = output_set_factory
        self._new_entity_factory = new_entity_factory

    def execute(self, input: Input) -> None:
        entity = self._new_entity_factory.create(**input.data)
        format_type = DataFormatType(input.output_type)
        outputter = self._output_set_factory.create(format_type=format_type, data=entity)
        outputter.output()
