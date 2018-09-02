from django import forms
# https://docs.djangoproject.com/en/dev/topics/forms/#form-objects

from .models import Note
# no model is used here
class InputText(forms.Form):
    inp_title = forms.CharField(label="Enter title ", max_length = 10000)
    inp_text = forms.CharField(label="Enter text  ", max_length = 10000,widget=forms.Textarea(attrs={'cols': 200, 'rows': 3}))


class InputTextQA(forms.Form):
    inp_title = forms.CharField(label="Enter title ", max_length = 10000)
    inp_text = forms.CharField(label="Enter text  ", max_length = 10000,widget=forms.Textarea(attrs={'cols': 200, 'rows': 3}))

def get_notes():
    return list(Note.objects.values_list("title", flat=True))
class DropDownTopic(forms.Form):
    li = get_notes()
    choice = []
    for l in li:
        t = (l, l)
        choice.append(t)
    inp_title = forms.CharField(label="Enter title ", max_length = 10000, required=True)    
    # topic = forms.ChoiceField(choices=choice)
    # topic = forms.ModelMultipleChoiceField(queryset=Note.objects.values_list("title", flat=True))
