from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import InputText, InputTextQA, DropDownTopic
import random
import string
import datetime
from elo.elo_interface import interface_elo as elo
# Create your views here.

#####################################################
#prod
def index(request):
    # test()
    dt = datetime.datetime.now()
    # li = list(Note.objects.values_list("title", flat=True, "words"))
    li = list(Note.objects.values("title", "words"))
    data = {"li": li, "ti":dt}
    # return HttpResponse(rv)
    return render(request, "elo/home/index.html", {"data": data})


def about(request):
    data = {"data:": "some text"}
    return render(request, "elo/home/about.html", {"data": data})

def test():
    n = Note(raw_text = "This is a test", sentences=1)
    n.save()

def search_db(request):
    comment = "In progress, IR search"
    data =  {"data":comment}
    return render(request, "elo/qa_db/search_db.html", {"data": data})


def get_db(request):
    title = list(Note.objects.values_list("title", flat=True))
    note = None
    cmd = "GET"
    form = DropDownTopic()
    if request.method == "POST":
        cmd = "POST"
        form = DropDownTopic(request.POST)
        if form.is_valid():
            topic = form.cleaned_data["inp_title"]
            note = Note.objects.filter(title=topic)
            # return HttpResponse("tile " + topic)
            cmd = "hm...."
            data = {"title":title, "note":note, "cmd":cmd, "form":form}
            return render(request, "elo/qa_db/get_db.html", {"data":data})
        else:
    # GET
    else:
        title = list(Note.objects.values_list("title", flat=True))
        form = DropDownTopic()
    data = {"title":title, "note":note, "cmd":cmd, "form":form}
    return render(request, "elo/qa_db/get_db.html", {"data": data})


@login_required
def delete_db(request):
    comment = "In progress, delete db"
    data =  {"data":comment}
    return render(request, "elo/qa_db/delete_db.html", {"data": data})


@login_required
def insert_db(request):
    if request.method == "POST":
        form = InputTextQA(request.POST)
        if form.is_valid():
            inp_title = form.cleaned_data["inp_title"]
            inp_text = form.cleaned_data["inp_text"]
            dt = " Process with elo"
            # process inp with elo
            # elo_blob = elo.Elo().text_summary(inp)
            tu = elo.Elo().text_insert(inp_text)
            note = Note(title=inp_title, raw_text=tu[0], sentences=tu[1], words=tu[2])
            note.save()
            rv = "Text saved with id: " + format(note.id)
            data = {"inp":inp_text, "dt":dt,"elo":tu, "rv":rv}
            return render(request, "elo/qa_db/insert_result.html", {"data": data})
            # return HttpResponse("yes...." + data)
            
    else:
        form = InputText()
    return render(request, "elo/qa_db/insert_db.html", {"form": form})


@login_required
def test_model(request):
    rv = "E-loweb, django admin testit.tech/admin. "
    # test()
    data = Note.objects.all()
    amount = Note.objects.count()
    context = {"data": data, "amount": amount}
    rv += format(context)
    # return HttpResponse(rv)
    return render(request, "elo/qa_db/test_model.html", context)


# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication
@login_required
def test_db_template(request):
    r = random.randint(0, 50)
    rr = random.randint(0, 10)
    li = [1,2,r,rr]
    tm = random.choice(string.ascii_letters)
    tmm = random.choice(string.ascii_letters)
    tmmm = random.choice(string.ascii_letters)
    tag = tm + tmm + tmmm
    data = {"tag":"a test tag " + tag, "li":li}
    return render(request, "elo/qa_db/test_db_template.html", {"data": data})


def test_rest(request):
    data = {}
    return render(request, "elo/qa_db/test_rest.html", data)

def error_404(request):
    data = {"data":404}
    return render(request, "elo/404.html", data)

def error_500(request):
    data = {"data":500}
    return render(request, "elo/500.html", data)
