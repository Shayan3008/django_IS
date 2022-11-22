from channels.generic.websocket import WebsocketConsumer
import json
class ChatConsumer(WebsocketConsumer):

      def connect(self):
          self.accept()
          self.send(json.dumps({
               "type":"Connection establish",
               "msg":"Congrats"
          }))
