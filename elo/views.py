from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Note
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

