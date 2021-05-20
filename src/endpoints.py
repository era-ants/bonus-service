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
from fastapi import status
from src import error_messages
from src.dependencies import get_db_session

router = APIRouter()


@router.get("/", response_model=schemas.HelloMessage, responses=error_messages.ERROR_MSG)
async def root(session=Depends(get_db_session)):
    """Endpoint return first user"""

    user = data_manager.first_user(session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Could not found any users",
        )
    message: str = service.get_hello_message_for_user(user)
    return schemas.HelloMessage(message=message)


@router.websocket("create-account")
async def create_bonus_account(websocket: WebSocket):

# await websocket.accept()
# while True:
#     data = await websocket.receive_text()
#     await websocket.send_text(f"Message text was: {data}")
