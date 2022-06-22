from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
import requests
from .forms import SearchUser
import json
# Create your views here.


def home(response):
    data = requests.get(
        'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/ReallyBlue/NA1?api_key=RGAPI-6c5d9a2c-3341-4b0c-a0a5-7eafe46e54cf')
    userid = data.json()['puuid']
    return render(response, "main/home.html", {
        'form': SearchUser(),  # include reference to your form
        'userid': userid,
        # 'mmr': apidata['rank']
    })


def search(response):
    form = SearchUser()
    return render(response, "main/home.html", {"form": form})
