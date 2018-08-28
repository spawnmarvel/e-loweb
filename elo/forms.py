from django import forms
# https://docs.djangoproject.com/en/dev/topics/forms/#form-objects

from .models import Note
# no model is used here
class InputText(forms.Form):
    inp_text = forms.CharField(label="Enter text  ", max_length = 10000,widget=forms.Textarea(attrs={'cols': 200, 'rows': 3}))


class InputTextQA(forms.Form):
    inp_text = forms.CharField(label="Enter text  ", max_length = 10000,widget=forms.Textarea(attrs={'cols': 200, 'rows': 3}))

class DropDownTopic(forms.Form):
    li = list(Note.objects.values_list("title", flat=True))
    choice = []
    for l in li:
        t = (l, l)
        choice.append(t)
    topic = forms.ChoiceField(choices=choice)
