from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import InputText, DropDownTopic, InputSearch
import random
import string
import datetime
from elo.elo_interface import interface_elo as elo
from django.db.models import Q
# Create your views here.

#####################################################
#prod
def index(request):
    # test()
    dt = ""# datetime.datetime.now()
    # li = list(Note.objects.values_list("title", flat=True, "words"))
    li = "" # list(Note.objects.values("title", "words", "hook"))
    data = {"li": li, "ti":dt}
    # return HttpResponse(rv)
    return render(request, "elo/home/index.html", {"data": data})


def about(request):
    data = {"data:": "some text"}
    return render(request, "elo/home/about.html", {"data": data})

def get_meta(request):
    dt = datetime.datetime.now()
    li = list(Note.objects.values("title", "words", "hook"))
    fi = list(Note._meta.get_fields())
    data = {"li":li, "ti":dt, "fi":fi}
    return render(request, "elo/qa_db/get_meta.html", {"data": data})

def search_db(request):
    comment = "GET 1"
    form = InputSearch()
    if request.method == "POST":
        form = InputSearch(request.POST)
        form.fields["choice"].initial = "title"
        if form.is_valid():
            get_note = ""
            hook = ""
            option = form.cleaned_data["choice"]
            inp_text = form.cleaned_data["inp_text"]
            if option == "title is":
                hook = "title is"
                get_note = Note.objects.filter(title=inp_text)
            elif option == "hook":
                hook = "hook"
                get_note = Note.objects.filter(hook=inp_text)
            elif option == "text contains":
                hook = "text contains"
                # a simple search, but install psql and search with that or cache
                get_note = Note.objects.filter(Q(raw_text__icontains=str(inp_text)))
            elif option == "word frequency high":
                hook = "word frequency high"
            elif option == "multiple words separated by comma":
                hook = "multiple words separated by comma"
            else:
                hook = "wtf"
            comment = "Started search with type: " + format(hook) + ":  for input: " + inp_text
            data =  {"comment":comment,"hook":hook,"note":get_note, "form":form}
            return render(request, "elo/qa_db/search_db.html", {"data": data, "form":form})
        else:
            pass
    # GET
    else:
        comment = "GET 2"
        form = InputSearch()
    data =  {"comment":comment, "form":form}
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
            pass
    # GET
    else:
        title = list(Note.objects.values_list("title", flat=True))
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
        form = InputText(request.POST)
        if form.is_valid():
            inp_title = form.cleaned_data["inp_title"]
            inp_text = form.cleaned_data["inp_text"]
            inp_hook = form.cleaned_data["inp_hook"]
            dt = " Process with elo"
            # process inp with elo
            # elo_blob = elo.Elo().text_summary(inp)
            tu = elo.Elo().text_insert(inp_text)
            note = Note(title=inp_title, raw_text=tu[0], sentences=tu[1], words=tu[2], hook=inp_hook)
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
