from http.client import responses
from django.shortcuts import render
from .forms import SearchUser
from .search import search


def home(request):
    if request.method == "POST":
        form = SearchUser(request.POST)
        if form.is_valid():
            form.cleaned_data["name"]
        else:
            return render(request, "main/home.html", {
                'form': SearchUser(),  # Reference to form
                'userid': search(request),
                # 'mmr':NA,
            })
