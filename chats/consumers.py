from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync
class ChatConsumer(WebsocketConsumer):

      def connect(self):
          self.room_group_name = "EMAIL"
          async_to_sync(self.channel_layer.group_add)(
               self.room_group_name,
               self.channel_name
          )
          self.accept()
          self.send(json.dumps({
               "type":"Connection establish",
               "msg":"Congrats"
          }))
      def receive(self,text_data):
           text_data_json = json.loads(text_data)
           message = text_data_json["message"]
           self.send(json.dumps({
               "type":"chat",
               "msg":message
          }))
     
          
