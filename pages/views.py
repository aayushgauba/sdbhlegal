from django.shortcuts import render, HttpResponse, redirect
from .models import Contact

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def expertise(request):
    return render(request, "expertise.html")

def choose(request):
    return render(request, "choose.html")

def sitemap(request):
    return HttpResponse(open('sitemap.xml').read(), content_type='text/xml')

def mediation(request):
    return render(request, "mediation.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        return redirect('contact')
    return render(request, "contact.html")