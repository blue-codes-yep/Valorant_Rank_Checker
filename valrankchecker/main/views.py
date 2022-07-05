from django.shortcuts import redirect, render
from django.shortcuts import HttpResponse
from .forms import SearchUser
from .search import search


def home(request):
    rank = ''
    form = ''
    if request.method == "POST":
        form = SearchUser(request.POST)
        if form.is_valid():
            print('form is coming')
            name = form.cleaned_data["name"]
            print(name)
            rank = search(request)
            return render(request, 'main/home.html', {'form': form, 'rank': rank})
    else:
        form = SearchUser()
        rank = search(request)
    return render(request, "main/home.html", {
        'form': form,  # Reference to form
        'rank': rank,
        # 'mmr':NA,
    })
