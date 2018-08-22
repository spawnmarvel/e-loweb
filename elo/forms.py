from django import forms
# https://docs.djangoproject.com/en/dev/topics/forms/#form-objects

# no model is used here
class InputText(forms.Form):
    inp_text = forms.CharField(label="Enter text  ", max_length = 10000)
