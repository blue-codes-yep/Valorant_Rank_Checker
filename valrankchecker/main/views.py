from django.shortcuts import redirect, render
from django.shortcuts import HttpResponse
from .forms import SearchUser
from .search import search


def home(request):
    rank = ''
    rr = ''
    form = ''
    if request.method == "POST":
        form = SearchUser(request.POST)
        if form.is_valid():
            print('form is coming')
            id = form.cleaned_data["id"]
            print(id)
            rank = search(request)
            rr = search(request)
            return render(request, 'main/home.html', {'form': form, 'rank': rank[0], 'rr': rr[1]})
    else:
        form = SearchUser()
        rank = search(request)
        rr = search(request)
    return render(request, "main/home.html", {
        'form': form,  # Reference to form
        'rank': rank,
        'rr': rr,
        # 'mmr':NA,
    })
