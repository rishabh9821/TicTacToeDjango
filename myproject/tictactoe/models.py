from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Game(models.Model):
    room_code = models.CharField(max_length = 100, unique = True)
    game_creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')
    game_opponent = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null = True)
    is_over = models.BooleanField(default = False)
    winner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='winner', blank = True, null = True)
