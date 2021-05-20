"""
Module: api.py
Author: vgolubev

Main module in project. Configure FastAPI application, include API routes, check and create database tables (if needed),
start async http server.
"""

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src import database
from src import config
from src import endpoints

app = FastAPI(title="API")

origins = [
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["OPTIONS", "GET", "POST", "PUT",],
    allow_headers=["*"],
)
app.include_router(endpoints.router, tags=["bonus account"])

database.init_db()

if __name__ == "__main__":
    uvicorn.run(app, host=config.IP_ADDR, port=config.HOST_PORT, log_level="info")
