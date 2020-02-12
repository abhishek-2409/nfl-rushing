from django.shortcuts import render, HttpResponse
from .models import Player

def index(request):
    players = Player.objects.all()
    params = {'players':players}
    return render(request, 'index.html', params)