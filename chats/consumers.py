from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync
from chats.models import Chats, KeyRoom
from chats.audio.audioEncryption import audioEncrypt
from kellanb_cryptography import aes, key

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.room_group_name = self.scope['url_route']['kwargs']['groupid']
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        keys = KeyRoom.objects.filter(groupId=self.room_group_name)
        if len(keys) > 0:
            print('This is the keys:', len(keys))
            self.keys = keys[0].key
        else:
            self.keys = key.gen_random_key()
            KeyRoom.objects.create(groupId=self.room_group_name, key=self.keys)
        self.accept()
        self.send(json.dumps({
            "type": "Connection establish",
            "msg": "Congrats"
        }))

    def receive(self, text_data):
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

            cipher_text = aes.encrypt_aes(message, self.keys)
            Chats.objects.create(
                sender=text_data_json["sender"],
                receiver=text_data_json["receiver"],
                groupId=self.room_group_name,
                EncryptedText=cipher_text
            )
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat_message",
                    "message": cipher_text,
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
                "message": aes.decrypt_aes(message, self.keys),
                "sender": event["sender"],
                "receiver": event["receiver"],
                "groupId": self.room_group_name
            }))

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
