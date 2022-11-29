import base64
from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync
import shutil
from chats.audio.audioEncryption import audioEncrypt


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        
        self.room_group_name = self.scope['url_route']['kwargs']['groupid']
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        print(self.channel_name)
        self.accept()
        self.send(json.dumps({
            "type": "Connection establish",
            "msg": "Congrats"
        }))

    def receive(self, text_data):
        # print(text_data["type"])
        text_data_json = json.loads(text_data)
        
        message = text_data_json["message"]
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message
            }
        )

    def chat_message(self, event):
        message = event["message"]
        print(message)
        self.send(json.dumps({
            "type": "chat",
            "message": message
        }))

    def disconnect(self,code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        
        
