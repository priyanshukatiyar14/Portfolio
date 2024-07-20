from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('projects/', projects_view, name='projects'),
    path('experiences/', experiences_view, name='experiences'),
    path('skills/', skills_view, name='skills'),
    
]
