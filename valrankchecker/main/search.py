import requests

def search(request):
    name = request.POST.get('name', 'novalue')
    if name != 'novalue':
        print('--------------------------------')
        print(name)
        print('--------------------------------')

        data = requests.get(
            f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{name}/NA1?api_key=RGAPI-f585b751-1b3b-409a-bb9c-6960f69cfa2d")
        print(data.url)
        try:

            puuid = data.json()['puuid']

            if puuid:
                print('-------------------this is ppuid-------------')
                print(puuid)
                print('-------------------this is ppuid-------------')
                print(name, 'has come here, means 200')
                return puuid
        except:
            print(name, 'has come here, means not found or forbidden')

            return 'puuid not found'