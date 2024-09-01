from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def expertise(request):
    return render(request, "expertise.html")

def choose(request):
    return render(request, "choose.html")

def mediation(request):
    return render(request, "mediation.html")

def contact(request):
    return render(request, "contact.html")