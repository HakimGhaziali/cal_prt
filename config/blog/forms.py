from django import forms

class MyForm(forms.Form):

    part_number = forms.CharField()
    today_dollar = forms.CharField()


class VariableForm(forms.Form):
    
    
    X = forms.CharField()