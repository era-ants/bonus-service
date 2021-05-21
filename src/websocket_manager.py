import websockets
import asyncio
from config import CLIENT_SERVICE_URL


def subscribe_for_client_signup():
        uri = f"ws://{CLIENT_SERVICE_URL}/clientshub"
        async with websockets.connect(uri) as websocket:
            while True:
                await websocket.send("sub")
                response = await websocket.recv()
                if response:
                    break
                asyncio.sleep(60)
