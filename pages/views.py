from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def expertise(request):
    return render(request, "expertise.html")

def choose(request):
    return render(request, "choose.html")

def sitemap(request):
    return HttpResponse(open('templates/sitemap.xml').read(), content_type='text/xml')

def mediation(request):
    return render(request, "mediation.html")

def contact(request):
    return render(request, "contact.html")