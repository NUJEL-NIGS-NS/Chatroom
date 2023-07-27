from channels.consumer import AsyncConsumer
from channels.exceptions import StopConsumer
import json
from channels.db import database_sync_to_async
from . models import *



class ChatConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        await self.send({
            'type': 'websocket.accept',
        })
        self.group_nam = self.scope['url_route']['kwargs']['group']
        await self.channel_layer.group_add(self.group_nam, self.channel_name)
      
            

    async def websocket_receive(self, event):
        dat = json.loads(event['text'])
        data = json.dumps(dat)
        print(type(dat))
        await self.channel_layer.group_send(
            self.group_nam,
            {
                'type': 'chat.message',
                'dsta': data
            }
        )
        Group_obj = await database_sync_to_async(Group.objects.get)(name=self.group_nam)
        chat = Chat(
            content=dat['Message'],
            name=dat['name'],
            group=Group_obj
        )

        await database_sync_to_async(chat.save)()


    async def chat_message(self, event):
        await self.send({
            'type': 'websocket.send',
            'text': event['dsta']
        })

    async def websocket_disconnect(self, event):
        print("hai.....")
