import os
from dotenv import load_dotenv
from sqlmodel import create_engine, Session
from ..infra.order_repository import OrderRepository
from ..application.usecase import NewOrder


def main():
    engine = create_engine(os.environ["CONNECTION_STRINGS"])
    with Session(engine) as session, session.begin():
        repository = OrderRepository(session=session)
        add_items = NewOrder(repository=repository)
        add_items.exec()


if __name__ == "__main__":
    load_dotenv()
    main()