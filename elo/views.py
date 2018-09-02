from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import InputText, InputTextQA, DropDownTopic
import random
import string
from elo.elo_interface import interface_elo as elo
# Create your views here.

#####################################################
#prod
def index(request):
    rv = "E-loweb, django admin testit.tech/admin. "
    # test()
    data = ""
    context = {"data": data}
    rv += format(context)
    # return HttpResponse(rv)
    return render(request, "elo/home/index.html", context)


def about(request):
    data = ""
    context = {"data": data}
    return render(request, "elo/home/about.html", context)

def test():
    n = Note(raw_text = "This is a test", sentences=1)
    n.save()

def process_text(request):
    if request.method == "POST":
        form = InputText(request.POST)
        if form.is_valid():
            data = form.cleaned_data["inp_text"]
            data += " Text from user"
            return render(request, "elo/prod_text/text_result.html", {"data": data})
            # return HttpResponse("yes...." + data)
            
    else:
        form = InputText()
    return render(request, "elo/prod_text/text_submit.html", {"form": form})


###################################
#qa
@login_required
def test_model(request):
    rv = "E-loweb, django admin testit.tech/admin. "
    # test()
    data = Note.objects.all()
    amount = Note.objects.count()
    context = {"data": data, "amount": amount}
    rv += format(context)
    # return HttpResponse(rv)
    return render(request, "elo/qa_text/test_model.html", context)


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
    return render(request, "elo/qa_db/test_submit_db.html", {"data": data})

@login_required
def test_get_processed_db(request):
    title = list(Note.objects.values_list("title", flat=True))
    note = None
    cmd = "GET"
    form = DropDownTopic()
    if request.method == "POST":
        cmd = "POST"
        form = DropDownTopic(request.POST)
        if form.is_valid():
            # topic = form.cleaned_data["topic"]
            topic = form.cleaned_data["inp_title"]
            # rv = topic
            note = Note.objects.filter(title=topic)
            # return HttpResponse("tile " + topic)
            cmd = "hm...."
            data = {"title":title, "note":note, "cmd":cmd, "form":form}
            return render(request, "elo/qa_db/test_db_result.html", {"data":data})
        else:
            fetch_text ="not valid form"
    # GET
    else:
        title = list(Note.objects.values_list("title", flat=True))
        form = DropDownTopic()
    data = {"title":title, "note":note, "cmd":cmd, "form":form}
    # return render(request, "elo/qa_db/test_db_result.html",{"data": data})
    return render(request, "elo/qa_db/test_db_result.html", {"data": data})


def test_process_text(request):
    if request.method == "POST":
        form = InputTextQA(request.POST)
        if form.is_valid():
            inp_title = form.cleaned_data["inp_title"]
            inp_text = form.cleaned_data["inp_text"]
            dt = " Process with elo"
            # process inp with elo
            # elo_blob = elo.Elo().text_summary(inp)
            elo_blob = elo.Elo().text_insert(inp_text)
            elo_list = elo_blob
            note = Note(title=inp_title, raw_text=inp_text, sentences=12)
            note.save()
            data = {"inp":inp_text, "dt":dt,"elo":elo_blob}
            return render(request, "elo/qa_text/test_submited_result.html", {"data": data})
            # return HttpResponse("yes...." + data)
            
    else:
        form = InputText()
    return render(request, "elo/qa_text/test_submit_text.html", {"form": form})

def test_rest(request):
    data = {}
    return render(request, "elo/qa_text/test_rest.html", data)

def error_404(request):
    data = {"data":404}
    return render(request, "elo/404.html", data)

def error_500(request):
    data = {"data":500}
    return render(request, "elo/500.html", data)
