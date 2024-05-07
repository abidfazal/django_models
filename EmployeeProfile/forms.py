from django import forms 


class NameForm(forms.Form):
    
    your_name = forms.CharField(label='your name',max_length=100)
    f_name = forms.CharField(label='father name ',max_length=100)