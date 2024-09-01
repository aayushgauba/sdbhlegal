from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('about', views.about, name='about'),
    path('expertise', views.expertise, name='expertise'),
    path('choose', views.choose, name='choose'),
    path('mediation', views.mediation, name='mediation'),
    path('contact', views.contact, name='contact'),
    path('sitemap', views.sitemap, name='sitemap'),
]