from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync
import shutil
from chats.audio.audioEncryption import audioEncrypt

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.room_group_name = "EMAIL"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        self.send(json.dumps({
            "type": "Connection establish",
            "msg": "Congrats"
        }))

    def receive(self, text_data):
        print(text_data)
        text_data_json = json.loads(text_data)
        if text_data_json["type"] == "download":
          shutil.copy2(text_data_json["path1"],text_data_json["path2"])
          audioEncrypt()
        else:
          message = text_data_json["message"]
          async_to_sync(self.channel_layer.group_send)(
               self.room_group_name,
               {
                    "type":"chat_message",
                    "message":message
               }
          )
    def chat_message(self,event):
        message = event["message"]
        self.send(json.dumps({
            "type":"chat",
            "message":message
        }))