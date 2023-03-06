from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        "msg" : "Seja bem-vindo a minha aplicacao com django.",
        "list": [1, 2, 3, 4, 5]
    }
    return render(request, "index.html", context)


