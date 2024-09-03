from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('about', views.about, name='about'),
    path('expertise', views.expertise, name='expertise'),
    path('choose', views.choose, name='choose'),
    path('mediation', views.mediation, name='mediation'),
    path('contact', views.contact, name='contact'),
    path('sitemap', views.sitemap, name='sitemap'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)