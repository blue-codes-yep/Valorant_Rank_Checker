from django.shortcuts import redirect, render
from django.shortcuts import HttpResponse
from .forms import SearchUser
from .search import search


def home(request):
    user_id = ''
    form = ''
    if request.method == "POST":
        form = SearchUser(request.POST)
        if form.is_valid():
            print('form is coming')
            name = form.cleaned_data["name"]
            print(name)
            user_id = search(request)
            return render(request, 'main/home.html', {'form': form, 'userid': user_id})
    else:
        form = SearchUser()
        user_id = search(request)
    return render(request, "main/home.html", {
        'form': form,  # Reference to form
        'userid': user_id,
        # 'mmr':NA,
    })
