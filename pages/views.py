from django.shortcuts import render, HttpResponse, redirect
from .models import Contact
from indexnow import IndexNow
import requests

def index(request):
    updated_url = "https://www.sdbhlegal.com"
    indexnow = IndexNow(key="7f3322dd1da64affa340bcb94eabc61a", host="sdbhlegal.com")
    indexnow.index([updated_url])
    return render(request, "index.html")

def about(request):
    updated_url = "https://www.sdbhlegal.com/about"
    indexnow = IndexNow(key="7f3322dd1da64affa340bcb94eabc61a", host="sdbhlegal.com")
    indexnow.index([updated_url])
    return render(request, "about.html")

def expertise(request):
    updated_url = "https://www.sdbhlegal.com/expertise"
    indexnow = IndexNow(key="7f3322dd1da64affa340bcb94eabc61a", host="sdbhlegal.com")
    indexnow.index([updated_url])
    return render(request, "expertise.html")

def choose(request):
    updated_url = "https://www.sdbhlegal.com/choose"
    indexnow = IndexNow(key="7f3322dd1da64affa340bcb94eabc61a", host="sdbhlegal.com")
    indexnow.index([updated_url])
    return render(request, "choose.html")

def sitemap(request):
    return HttpResponse(open('sitemap.xml').read(), content_type='text/xml')

def mediation(request):
    updated_url = "https://www.sdbhlegal.com/mediation"
    indexnow = IndexNow(key="7f3322dd1da64affa340bcb94eabc61a", host="sdbhlegal.com")
    indexnow.index([updated_url])    
    return render(request, "mediation.html")

def contact(request):
    updated_url = "https://www.sdbhlegal.com/contact"
    indexnow = IndexNow(key="7f3322dd1da64affa340bcb94eabc61a", host="sdbhlegal.com")
    status = indexnow.index([updated_url])
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        contact = Contact(name=name, email=email, message=message, mailSent = False)
        contact.save()
        return redirect('contact')
    return render(request, "contact.html")