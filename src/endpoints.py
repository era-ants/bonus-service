"""
Module: endpoints.py
Author: vgolubev

Module describe API Endpoints.  
"""

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import WebSocket

from src import service
from src import data_manager
from src import schemas
from src import error_messages
from src.dependencies import get_db_session

router = APIRouter()


@router.post("/", response_model=schemas.Account, status_code=201,
             responses=error_messages.ACCOUNT_ALREADY_EXIST['api_docs'])
async def create_account(account: schemas.CreateAccount, session=Depends(get_db_session)):
    """Endpoint for creating bonus account"""

    account = data_manager.create_account(session, account)
    if not account:
        raise HTTPException(**error_messages.ACCOUNT_ALREADY_EXIST['exception'])
    return account


@router.get("/{client_id}", response_model=schemas.Account, status_code=200,
             responses=error_messages.ACCOUNT_ALREADY_EXIST['api_docs'])
async def get_account(client_id: int, session=Depends(get_db_session)):
    """Endpoint return account with Client ID"""

    account = data_manager.get_client_account(session, client_id)
    if not account:
        raise HTTPException(**error_messages.ACCOUNT_ALREADY_EXIST['exception'])
    return account


@router.websocket("create-account")
async def create_bonus_account(websocket: WebSocket):
    pass
# await websocket.accept()
# while True:
#     data = await websocket.receive_text()
#     await websocket.send_text(f"Message text was: {data}")
