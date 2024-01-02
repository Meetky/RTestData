import json
from socket_demo.return_msg import *
import asyncio
import websockets


async def echo(websocket, path):
    while True:
        message = await websocket.recv()
        print(message)
        print(type(message))
        if message is None:
            break
        if message == "2d":
            return_msg = json.dumps(resource2d.main())
            await websocket.send(return_msg)
        elif message == "sign":
            return_msg = json.dumps(sign.main(3))
            await websocket.send(return_msg)
        else:
            await websocket.send("Unknown Message")


start_server = websockets.serve(echo, "0.0.0.0", 7071)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
