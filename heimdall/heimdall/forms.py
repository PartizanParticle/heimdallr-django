from django import forms

class heightForm(forms.Form):
    door_height = forms.FloatField(label='Door Height in CM', max_value=4000)
