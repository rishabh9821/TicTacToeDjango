from django.urls import path
from tictactoe.consumers import GameRoom

ws_patterns = [
    path('ws/game/<room_code>', GameRoom.as_asgi())
]