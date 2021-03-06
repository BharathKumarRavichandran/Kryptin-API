import asyncio
import json

from django.contrib.auth import get_user_model

from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async

from .models import User, Message


class ChatConsumer(AsyncConsumer):
    
    async def websocket_connect(self, event):

        print("Websocket connected :", event)

        await self.send({
            "type": "websocket.accept"
        })

        await self.send({
            "type": "websocket.send",
            "data": "Websocket connected"
        })


    async def websocket_receive(self, event):

        print("Websocket received data :", event)

        from_username = ''
        to_username   = ''
        message       = ''
        text          = event.get('text', None)
        data          = json.loads(text).get('data')
         
        if data is not None :

            from_username = data['fromUsername']
            to_username   = data['toUsername']
            message       = data['message']

            send_data = ({
                "from_username" : from_username,
                "to_username"   : to_username,
                "message"       : message
            })

            try:
                from_user = User.objects.get(username=from_username)
                to_user   = User.objects.get(username=to_username)

            except User.DoesNotExist:
                print("User does not exist")
                return "User does not exist"

            user_message = Message.objects.create(from_user=from_user, to_user=to_user, message=message)

            await self.send({
                "type" : "websocket.send",
                "data" : json.dumps(send_data)
            })


    async def websocket_disconnect(self, event):

        print("Websocket disconnected :", event)

        await self.send({
            "type": "websocket.send",
            "data": "Websocket disconnected!"
        })

        await self.send({
            "type": "websocket.close"
            })
