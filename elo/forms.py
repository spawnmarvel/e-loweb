from django import forms
# https://docs.djangoproject.com/en/dev/topics/forms/#form-objects

from .models import Note
# no model is used here
class InputText(forms.Form):
    inp_hook = forms.CharField(label="Enter data hook ", max_length = 20)
    inp_title = forms.CharField(label="Enter title ", max_length = 100)
    inp_text = forms.CharField(label="Enter text  ", max_length = 10000,widget=forms.Textarea(attrs={'cols': 200, 'rows': 3}))
   

class InputTextQA(forms.Form):
    inp_title = forms.CharField(label="Enter title ", max_length = 100)
    inp_text = forms.CharField(label="Enter text  ", max_length = 10000,widget=forms.Textarea(attrs={'cols': 200, 'rows': 3}))
    inp_hook = forms.CharField(label="Enter hook ", max_length = 20)

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

class InputSearch(forms.Form):
    ch = (("title is", "title is"), ("hook", "hook"), ("text contains", "text contains"), ("word frequency high", "word frequency high"), ("multiple words separated by comma", "multiple words separated by comma"))
    choice = forms.ChoiceField(choices=ch)
    inp_text = forms.CharField(label="Enter text", max_length = 100)

