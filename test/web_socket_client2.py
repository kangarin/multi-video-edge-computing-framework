# import asyncio
# import websockets


# async def hello(uri):
#     async with websockets.connect(uri) as websocket:
#         await websocket.send("Hello world!")
#         recv_text = await websocket.recv()
#         print(recv_text)


# asyncio.get_event_loop().run_until_complete(
#     hello('ws://localhost:8567'))


import asyncio
import websockets
import time
from datetime import datetime

async def ws_client(url):
    for i in range(1, 40):
        async with websockets.connect(url) as websocket:
            await websocket.send("Hello, I am Client2.")
            response = await websocket.recv()
            reply = f"Data received as \"{response}\".  time: {datetime.now()}"
        print(reply)
        time.sleep(1)

asyncio.run(ws_client('ws://localhost:8567'))


