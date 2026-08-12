from uuid import UUID
import os
from dotenv import load_dotenv
from sqlmodel import create_engine, Session
from ..infra.order_repository import OrderRepository
from ..application.usecase import ChangeOrderState


def main():
    engine = create_engine(os.environ["CONNECTION_STRINGS"])
    with Session(engine) as session, session.begin():
        repository = OrderRepository(session=session)
        order_id = UUID("019ff654ec9a70ae83fe13f80a1d9764")
        operation = "CANCEL"
        change_state = ChangeOrderState(repository=repository)
        change_state.exec(order_id=order_id, operation_str=operation)


if __name__ == "__main__":
    load_dotenv()
    main()