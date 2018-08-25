from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import InputText
import random
import string
from elo.elo_interface import interface_elo as elo
# Create your views here.

def index(request):
    rv = "E-loweb, django admin testit.tech/admin. "
    # test()
    data = ""
    context = {"data": data}
    rv += format(context)
    # return HttpResponse(rv)
    return render(request, "elo/index.html", context)


def about(request):
    data = ""
    context = {"data": data}
    return render(request, "elo/about.html", context)

def test():
    n = Note(raw_text = "This is a test", sentences=1)
    n.save()

def process_text(request):
    if request.method == "POST":
        form = InputText(request.POST)
        if form.is_valid():
            data = form.cleaned_data["inp_text"]
            data += " Text from user"
            return render(request, "elo/submited_result.html", {"data": data})
            # return HttpResponse("yes...." + data)
            
    else:
        form = InputText()
    return render(request, "elo/submit_text.html", {"form": form})


# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication
@login_required
def process_db(request):
    r = random.randint(0, 50)
    rr = random.randint(0, 10)
    li = [1,2,r,rr]
    tm = random.choice(string.ascii_letters)
    tmm = random.choice(string.ascii_letters)
    tmmm = random.choice(string.ascii_letters)
    tag = tm + tmm + tmmm
    data = {"tag":"a test tag " + tag, "li":li}
    return render(request, "elo/submit_db.html", {"data": data})

def test_model(request):
    rv = "E-loweb, django admin testit.tech/admin. "
    # test()
    data = Note.objects.all()
    amount = Note.objects.count()
    context = {"data": data, "amount": amount}
    rv += format(context)
    # return HttpResponse(rv)
    return render(request, "elo/test_model.html", context)

def test_process_text(request):
    if request.method == "POST":
        form = InputText(request.POST)
        if form.is_valid():
            data = form.cleaned_data["inp_text"]
            data += " Text from user, add TextBlob, call elo"
             # elo_blob = elo.Elo().toString() + " test"
             # data = {"inp": inp, "elo": elo_blob}
            return render(request, "elo/test_submited_result.html", {"data": data})
            # return HttpResponse("yes...." + data)
            
    else:
        form = InputText()
    return render(request, "elo/test_submit_text.html", {"form": form})

# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication
@login_required
def test_process_db(request):
    r = random.randint(0, 50)
    rr = random.randint(0, 10)
    li = [1,2,r,rr]
    tm = random.choice(string.ascii_letters)
    tmm = random.choice(string.ascii_letters)
    tmmm = random.choice(string.ascii_letters)
    tag = tm + tmm + tmmm
    data = {"tag":"a test tag " + tag, "li":li}
    return render(request, "elo/test_submit_db.html", {"data": data})

        
def test_rest(request):
    data = {}
    return render(request, "elo/test_rest.html", data)

def error_404(request):
    data = {"data":404}
    return render(request, "elo/404.html", data)

def error_500(request):
    data = {"data":500}
    return render(request, "elo/500.html", data)
