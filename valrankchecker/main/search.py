import requests


def search(request):
    data = requests.get(
        f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{name}/NA1?api_key=RGAPI-d1224a2c-9130-45ff-8c05-0656d56d105f")
    return data.json()['puuid']
