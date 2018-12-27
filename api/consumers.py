import asyncio
import json

from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async

from .models import *

class ChatConsumer(AsyncConsumer):
    
    async def websocket_connect(self, event):

        print("Connected", event)

        await self.send({
            "type": "websocket.accept"
        })

        await self.send({
            "type": "websocket.send",
            "text": "Hello world"
        })

    async def websocket_receive(self, event):

        print("Receive", event)
        
        dict_data = ''
        message   = ''
        data = event.get('text', None)
        
        if data is not None:
            dict_data = json.loads(data)
            message   = dict_data.get('message')
            print(message)


    async def websocket_disconnect(self, event):

        print("Disconnect", event)

        await self.send({
            "type": "websocket.send",
            "text": "Hello world"
        })
