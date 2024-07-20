from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('contact_submit/', contact_submit, name='contact_submit') 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  

# static files url

