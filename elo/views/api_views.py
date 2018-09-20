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
    context["data"] = x
    t = json.dumps(context)
    return HttpResponse(t)