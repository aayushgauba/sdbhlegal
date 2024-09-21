from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('about', views.about, name='about'),
    path('expertise', views.expertise, name='expertise'),
    path('choose', views.choose, name='choose'),
    path('mediation', views.mediation, name='mediation'),
    path('contact', views.contact, name='contact'),
    path('sitemap', views.sitemap, name='sitemap'),
    path('76dfebe7687d4416a7d5cd0eda143fc8.txt', serve, {'document_root': settings.STATICFILES_DIRS[0], 'path': '7fcc06c5e3184e13ab70cae01c1e6126.txt'}),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)