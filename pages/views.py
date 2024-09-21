from django.shortcuts import render, HttpResponse, redirect
from .models import Contact
from indexnow import IndexNow
import os

indexnow = IndexNow(key="76dfebe7687d4416a7d5cd0eda143fc8", host="sdbhlegal.com")
urls_to_index = []

def submit_urls():
    global urls_to_index
    if urls_to_index:
        try:
            indexnow.index(urls_to_index)
        except Exception as e:
            # Silencing the error
            print(f"An error occurred: {e}")
        urls_to_index = []

def index(request):
    updated_url = "https://www.sdbhlegal.com"
    urls_to_index.append(updated_url)
    submit_urls()
    return render(request, "index.html")

def about(request):
    updated_url = "https://www.sdbhlegal.com/about"
    urls_to_index.append(updated_url)
    submit_urls()
    return render(request, "about.html")
    
def expertise(request):
    updated_url = "https://www.sdbhlegal.com/expertise"
    urls_to_index.append(updated_url)
    submit_urls()
    return render(request, "expertise.html")

def choose(request):
    updated_url = "https://www.sdbhlegal.com/choose"
    urls_to_index.append(updated_url)
    submit_urls()
    return render(request, "choose.html")

def sitemap(request):
    file_path = os.path.join(os.path.dirname(__file__), 'sitemap.xml')
    with open(file_path, 'r') as file:
        content = file.read()
    return HttpResponse(content, content_type='text/xml')

def mediation(request):
    updated_url = "https://www.sdbhlegal.com/mediation"
    urls_to_index.append(updated_url)
    submit_urls()
    return render(request, "mediation.html")

def contact(request):
    updated_url = "https://www.sdbhlegal.com/contact"
    urls_to_index.append(updated_url)
    submit_urls()
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        contact = Contact(name=name, email=email, message=message, mailSent=False)
        contact.save()
        return redirect('contact')
    return render(request, "contact.html")
