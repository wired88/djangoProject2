from django import forms


class MyForm(forms.Form):
    search_field = forms.CharField(label='Produkteingabe', max_length=25)

