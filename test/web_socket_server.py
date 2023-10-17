# import asyncio
# import websockets


# async def echo(websocket, path):
#     async for message in websocket:
#         message = "I got your message: {}".format(message)
#         await websocket.send(message)


# asyncio.get_event_loop().run_until_complete(websockets.serve(echo, 'localhost', 8567))
# asyncio.get_event_loop().run_forever()


#!/usr/bin/python3
# 主要功能：创建1个基本的websocket server, 符合asyncio 开发要求
import asyncio
import websockets
from datetime import datetime


async def handler(websocket):
    data = await websocket.recv()
    reply = f"Data received as \"{data}\".  time: {datetime.now()}"
    print(reply)
    reply_str = "I'm fine, thank you. And you?"
    await websocket.send(reply_str)
    # print("Send reply")


async def main():
    async with websockets.serve(handler, "localhost", 8567):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())


