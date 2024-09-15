from django import forms


class AboutBook(forms.Form):
    desc = forms.CharField(label='Описание книги')

class NameBook(forms.Form):
    name = forms.CharField(label ='Название книги')