import json
from socket_demo.return_msg import *
import asyncio
import websockets


async def echo(websocket, path):
    while True:
        message = await websocket.recv()
        print(message)
        if message is None:
            break
        try:
            if "sub_topic" not in message:
                if str(message) == "2d":
                    await websocket.send(
                        json.dumps({"ver": 1, "operation": 9, "body": [resource2d.main()], "topic": str(message)}))
                elif str(message) == "表格":
                    await websocket.send(
                        json.dumps({"ver": 1, "operation": 9, "body": [form.main_user(16)], "topic": str(message)}))
                elif str(message) == "标记":
                    await websocket.send(
                        json.dumps({"ver": 1, "operation": 9, "body": [sign.main(3)], "topic": str(message)}))
                elif str(message) == "飞线":
                    await websocket.send(
                        json.dumps({"ver": 1, "operation": 9, "body": [flyline.main(3)], "topic": str(message)}))
                else:
                    await websocket.send(
                        json.dumps({"ver": 1, "operation": 9, "body": ["Unknown Message"], "topic": "Unknown Message"}))
            elif "sub_topic" in message:
                message = json.loads(json.loads(message)["body"])
                sub_topic = message["sub_topic"]
                if sub_topic[0] == "2d":
                    await websocket.send(
                        json.dumps({"ver": 1, "operation": 9, "body": [resource2d.main()], "topic": str(message)}))
                elif sub_topic[0] == "sign":
                    await websocket.send(
                        json.dumps({"ver": 1, "operation": 9, "body": [sign.main(3)], "topic": str(message)}))
            else:
                await websocket.send(
                    json.dumps({"ver": 1, "operation": 9, "body": ["Unknown Message"], "topic": "Unknown Message"}))
                break
        except Exception as e:
            print(f"Error processing message: {e}")
            await websocket.send(
                json.dumps(
                    {"ver": 1, "operation": 9, "body": ["Invalid message format"], "topic": "Invalid message format"}))
            break


start_server = websockets.serve(echo, "0.0.0.0", 7071)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
