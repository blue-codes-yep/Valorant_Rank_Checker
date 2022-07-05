from django import forms


class SearchUser(forms.Form):
    id = forms.CharField(label="Name", max_length=200)
