from cgitb import text
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from tictactoe.models import Game
from django.contrib.auth.models import User
import json

class GameRoom(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_code']
        self.room_group_name = 'room_%s' % self.room_name

        print(self.room_group_name)

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
    
    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'run_game',
                'payload': text_data
            }
        )

    def run_game(self, event):
        data = event['payload']
        data = json.loads(data)

        if data['data']['type'] == 'end':
            print(data['data'])
            addGame(data)

        self.send(text_data = json.dumps({
            'payload': data['data']
        }))

def addGame(data):
    print('-----MODEL ADDED-----')
    game = Game.objects.get(room_code = data['data']['room_name'])
    game.is_over = True
    game.winner = User.objects.get(username = data['data']['username'])
    game.save()


