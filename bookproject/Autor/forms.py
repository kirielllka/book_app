from django import forms


class AuthorSearchForm(forms.Form):
    name = forms.CharField(label='Фамилия автора')



