import os

from dotenv import load_dotenv
from sqlmodel import Session, create_engine

from ..application.usecase import NewOrder
from ..infra.order_repository import OrderRepository


def main():
    engine = create_engine(os.environ["CONNECTION_STRINGS"])
    with Session(engine) as session, session.begin():
        repository = OrderRepository(session=session)
        add_items = NewOrder(repository=repository)
        add_items.exec()


if __name__ == "__main__":
    load_dotenv()
    main()
