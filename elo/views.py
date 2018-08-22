from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import InputText
# Create your views here.

def index(request):
    rv = "E-loweb, django admin testit.tech/admin. "
    # test()
    data = Note.objects.all()
    context = {"data": data}
    rv += format(context)
    # return HttpResponse(rv)
    return render(request, "elo/index.html", context)


def about(request):
    data = Note.objects.count()
    context = {"data": data}
    return render(request, "elo/about.html", context)

def test():
    n = Note(raw_text = "This is a test", sentences=1)
    n.save()

# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication
@login_required
def get_user_text(request):
    if request.method == "POST":
        form = InputText(request.POST)
        if form.is_valid():
            data = form.cleaned_data["inp_text"]
            data += "Well you made it"
            return render(request, "elo/submited_result.html", {"data": data})
            # return HttpResponse("yes...." + data)
            
    else:
        form = InputText()
    return render(request, "elo/submit_text.html", {"form": form})
        



