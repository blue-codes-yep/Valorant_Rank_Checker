from http.client import responses
from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import SearchUser
from .search import search


def home(request):
    user_id = ''
    form = ''
    if request.method == "POST":
        form = SearchUser(request.POST)
        print('form is coming')
        # form.cleaned_data["name"]
        #just for testing purpose you can remove it.
    else:
        form = SearchUser()
        user_id = search(request)
    return render(request, "main/home.html", {
        'form': form,  # Reference to form
        'userid': user_id,
        # 'mmr':NA,
    })

