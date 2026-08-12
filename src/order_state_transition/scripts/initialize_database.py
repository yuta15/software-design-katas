import os

from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine

from ..infra import schema  # noqa: F401


def initialize_database(conn_str: str) -> None:
    engine = create_engine(conn_str)
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    load_dotenv()
    conn_str = os.environ["CONNECTION_STRINGS"]
    print(conn_str)
    initialize_database(conn_str)
