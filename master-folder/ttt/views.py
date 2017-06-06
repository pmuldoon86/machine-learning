from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to tictactoe!")


# Create your views here.
