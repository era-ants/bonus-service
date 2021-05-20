from typing import Optional
from src import models
from src import schemas
from sqlalchemy.exc import IntegrityError


def create_account(session, account_credentials: schemas.CreateAccount) -> Optional[schemas.Account]:
    """"Add a bonus account to data store"""

    account = models.Account(id=account_credentials.client_id, bonus_count=0)
    session.add(account)
    try:
        session.commit()
    except IntegrityError:
        return None
    session.refresh(account)
    return schemas.Account(id=account.id, bonus_count=account.bonus_count)


def get_client_account(session, client_id: int):
    """"Select a bonus account with Client ID from data store"""

    return session.query(models.Account).filter(models.Account.id == client_id).first()
