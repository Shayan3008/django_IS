from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync
from chats.models import Chats, KeyRoom
from chats.audio.audioEncryption import audioEncrypt
from kellanb_cryptography import aes

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
            Chats.objects.create(
                sender=text_data_json["sender"],
                receiver=text_data_json["receiver"],
                groupId=self.room_group_name,
                Audio=text_data_json["message"])
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
            chat_key = KeyRoom.objects.filter(
                groupId=self.room_group_name)[0].key
            cipher_text = aes.encrypt_aes(message, chat_key)
            Chats.objects.create(
                sender=text_data_json["sender"],
                receiver=text_data_json["receiver"],
                groupId=self.room_group_name,
                Text=message,
                EncryptedText=cipher_text
            )
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat_message",
                    "message": message,
                    "type2": "chat",
                    "sender": text_data_json["sender"],
                    "receiver": text_data_json["receiver"],
                }
            )

    def chat_message(self, event):
        message = event["message"]
        type = event["type2"]
        if type == "audio":

            self.send(json.dumps({
                "type": "audio",
                "message": message,
                "sender": event["sender"],
                "receiver": event["receiver"],
                "groupId": self.room_group_name
            }))
        else:

            self.send(json.dumps({
                "type": "chat",
                "message": message,
                "sender": event["sender"],
                "receiver": event["receiver"],
                "groupId": self.room_group_name
            }))

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )