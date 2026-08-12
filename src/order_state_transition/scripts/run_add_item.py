import os
from uuid import UUID
from dotenv import load_dotenv
from sqlmodel import create_engine, Session
from ..infra.order_repository import OrderRepository
from ..application.usecase import AddItems


def main():
    engine = create_engine(os.environ["CONNECTION_STRINGS"])
    with Session(engine) as session, session.begin():
        repository = OrderRepository(session=session)
        add_items = AddItems(repository=repository)
        order_id = UUID("019ff654e34672ee9316bc7028b27fa7")
        item_name = "dummy-item3"
        item_price = 100
        add_items.exec(order_id=order_id, item_name=item_name, item_price=item_price)


if __name__ == "__main__":
    load_dotenv()
    main()