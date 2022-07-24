from django.shortcuts import render, redirect
from django.contrib import messages
from tictactoe.models import Game
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from tictactoe.forms import UserCreationForm
# Create your views here.

def signUpView(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = True)
            login(request, user)
            return HttpResponseRedirect(reverse_lazy('home'))
    else:
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form':form})


def AboutView(request):
    return render(request, 'about.html')


@login_required
def home(request):
    if request.method == 'POST':
        username = request.user
        optionPicked = request.POST.get('option')
        room_code = request.POST.get('room_code')

        if optionPicked == '1':
            game = Game(room_code = room_code)
            print(game)
            if game.game_opponent == None:
                game = Game.objects.get(room_code = room_code)
                game.game_opponent = username
                game.save()
                return redirect('play/' + room_code + '?username='+username.username)
            elif game == None:
                message = "Game is over"
                return render(request, 'home.html', {'messages': message})
            elif game.game_opponent != None:
                message =  'Already Has an Opponent'
                return render(request, 'home.html', {'messages': message})
            elif game.is_over():
                message =  'Game is over'
                return render(request, 'home.html', {'messages': message})
        elif optionPicked == '2':
            game = Game.objects.get_or_create(game_creator = username, 
                                              room_code = room_code)
            game[0].save()
            return redirect('play/' + room_code + '?username='+username.username)
    
    return render(request, 'home.html')

def play(request, room_code):
    username = request.GET.get('username')
    context = {'room_code': room_code,
                'username': username}
    
    return render(request, 'play.html', context = context)
            

