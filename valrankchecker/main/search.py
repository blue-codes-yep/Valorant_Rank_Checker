from valo_api import get_mmr_details_by_name_v1
from valo_api.exceptions.valo_api_exception import ValoAPIException


def search(request):
    id = request.POST.get('id', 'novalue')
    if id == 'novalue':
        return
    name, tag = id.split("#")
    try:
        print(f"{name=}; {tag=}")
        data = get_mmr_details_by_name_v1('na', name, tag)
        print(data)
        return data.currenttierpatched, data.ranking_in_tier
    except ValoAPIException as e:
        print(e)
