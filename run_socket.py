import json
from socket_demo.return_msg import *
import asyncio
import websockets


async def echo(websocket, path):
    try:
        while True:
            message = await websocket.recv()
            if message is None:
                break
            try:
                if "sub_topic" not in message:
                    raise ValueError("Missing 'sub_topic' field")
                message = json.loads(json.loads(message)["body"])
                sub_topic = message["sub_topic"]
                if not isinstance(sub_topic, list):
                    raise ValueError("Invalid 'sub_topic' format")
                if sub_topic[0] == "2d":
                    return_msg = json.dumps(resource2d.main())
                    await websocket.send(return_msg)
                elif sub_topic[0] == "sign":
                    return_msg = json.dumps(sign.main(3))
                    await websocket.send(return_msg)
                else:
                    await websocket.send("Unknown Message")
            except ValueError as e:
                print(f"Error processing message: {e}")
                await websocket.send("Invalid message format")
            await websocket.send("Client disconnected unexpectedly.")
    except websockets.ConnectionClosedOK:
        await websocket.send("Client disconnected unexpectedly.")


start_server = websockets.serve(echo, "0.0.0.0", 7071)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
