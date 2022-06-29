import requests
from .forms import SearchUser

def search(request):
    name=request.POST.get('name') 
    data = requests.get(
     f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{name}/NA1?api_key=RGAPI-d801ef44-e952-43b0-9b08-92badc7da82c")
    return data.json()['puuid']
