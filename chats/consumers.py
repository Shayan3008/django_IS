
from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync
from chats.models import Chats
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
        if text_data_json["type"] == "audio":
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat_message",
                    "message": text_data_json["message"],
                    "sender": text_data_json["sender"],
                    "receiver": text_data_json["receiver"],
                    "type2": "audio"
                }
            )
        else:
            message = text_data_json["message"]
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat_message",
                    "message": message,
                    "type2": "chat"
                }
            )

    def chat_message(self, event):
        message = event["message"]
        type = event["type2"]
        if type == "audio":
            Chats.objects.create(
                sender=event["sender"], receiver=event["receiver"], groupId=self.room_group_name, Audio=message)
            self.send(json.dumps({
                "type": "audio",
                "message": message,
                "sender": event["sender"], "receiver": event["receiver"], "groupId": self.room_group_name
            }))
        else:
            print(message)
            self.send(json.dumps({
                "type": "chat",
                "message": message
            }))

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
