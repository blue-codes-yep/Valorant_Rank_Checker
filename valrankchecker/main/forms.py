from django import forms


class SearchUser(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
