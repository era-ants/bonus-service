"""
Module: endpoints.py
Author: vgolubev

Module describe API Endpoints.  
"""

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import WebSocket
from fastapi import WebSocketDisconnect

from src import service
from src import data_manager
from src import schemas
from src import error_messages
from src.dependencies import get_db_session

router = APIRouter()


@router.post("/bonus", status_code=200, responses=error_messages.ACCOUNT_DOES_NOT_EXIST['api_docs'])
async def add_bonus_to_account(account: schemas.Account, session=Depends(get_db_session)):
    """Endpoint for add bonus to account"""

    bonus_count = data_manager.add_bonus_to_account(session, account)
    if not bonus_count:
        raise HTTPException(**error_messages.ACCOUNT_DOES_NOT_EXIST['exception'])
    return bonus_count


@router.get("/{client_id}", response_model=schemas.Account, status_code=200,
            responses=error_messages.ACCOUNT_ALREADY_EXIST['api_docs'])
async def get_account(client_id: int, session=Depends(get_db_session)):
    """Endpoint return account with Client ID"""

    account = data_manager.get_client_account(session, client_id)
    if not account:
        raise HTTPException(**error_messages.ACCOUNT_ALREADY_EXIST['exception'])
    return account


@router.websocket("create-account")
async def create_bonus_account(websocket: WebSocket, session=Depends(get_db_session)):
    await websocket.accept()
    try:
        account_data = await websocket.receive_json()
        account = data_manager.create_account(session, account_data)
        if account:
            await websocket.send_json({'message': 'ok'})
        else:
            await websocket.send_json(error_messages.ACCOUNT_ALREADY_EXIST['exception'])
    except WebSocketDisconnect:
        pass
