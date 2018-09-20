import json
from elo.models import Note
from django.http import HttpResponse



# API
def api_get_meta(request):
    obj = Note.objects.all()
    context = {}
    context["status"] = 200
    x = []
    y = []
    for n in obj:
        x.append("Id: " + str(n.id) + ". " + "Title: "+ str(n.title) + ". Hook: " + str(n.hook) + ". Words: "+ str(n.words))
    context["data meta"] = x
    t = json.dumps(context)
    return HttpResponse(t)

def api_get_hook(request, db_hook):
    obj = Note.objects.filter(hook=db_hook)
    x = []
    context = {}
    for d in obj:
        x.append("Id: " + str(d.id) + ". Text: " + str(d.raw_text))
    context["data all by hook"] = x
    t = json.dumps(context)
    return HttpResponse(t) 