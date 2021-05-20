"""
Module: schemas.py
Author: vgolubev

Module describe pydantic schemas for requests and responses.  
"""

from typing import List, Optional
from pydantic import BaseModel


class HelloMessage(BaseModel):
    message: str


class CreateAccount(BaseModel):
    client_id: int


class GetAccount(BaseModel):
    client_id: int


class Account(BaseModel):
    id: int
    bonus_count: int

    class Config:
        orm_mode = True
