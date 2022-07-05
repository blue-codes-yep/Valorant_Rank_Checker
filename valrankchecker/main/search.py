import valo_api


def search(request):
    name = request.POST.get('name', 'novalue')
    if name != 'novalue':
        print('--------------------------------')
        print(name)
        print('--------------------------------')

        data = valo_api.get_mmr_details_by_name_v1('na', name, 'NA1')
        data = data.__dict__
        try:
            print(data)
            if data:
                print('-------------------this is data-------------')
                print(data)
                print('-------------------this is data-------------')
                print(name, 'has come here, means 200')
                return data.get(('currenttierpatched'))
        except Exception as e:
            print(e)
