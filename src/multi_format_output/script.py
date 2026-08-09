from infra import JsonOutputter, JsonDataFormatter, CSVDataFormatter, CsvOutputter, TSVDataFormatter, TsvOutputter, ImpleOutputSetFactory, OutputSetDependencies, UuidIdGenerater
from domain import NewEntityFactory

from application import Usecase, Input


def main():
    dependencies = OutputSetDependencies(
        json_formatter=JsonDataFormatter,
        csv_formatter=CSVDataFormatter,
        tsv_formatter=TSVDataFormatter,
        json_outputter=JsonOutputter,
        csv_outputter=CsvOutputter,
        tsv_outputter=TsvOutputter,
    )
    output_set_factory = ImpleOutputSetFactory(dependencies)
    new_entity_factory = NewEntityFactory(id_generater=UuidIdGenerater())
    uc = Usecase(output_set_factory=output_set_factory, new_entity_factory=new_entity_factory)

    input = Input(data={"name": "michi", "age": 26}, output_type="JSON")
    uc.execute(input=input)


if __name__ == "__main__":
    main()