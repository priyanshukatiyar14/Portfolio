from django.shortcuts import render
from .models import AboutMe, Skill, Project, Experience
from .forms import ContactForm

def home(request):
    about_me = AboutMe.objects.first()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()
    return render(request, 'templates/index.html', {
        'about_me': about_me,
        'skills': skills,
        'projects': projects,
        'experiences': experiences,
        'form': form
    })

def about_view(request):
    # Your logic here
    return render(request, 'about.html', {})

def contact_view(request):
    # Your logic here
    return render(request, 'contact.html', {})

def projects_view(request):
    # Your logic here
    return render(request, 'projects.html', {})

def experiences_view(request):
    # Your logic here
    return render(request, 'experiences.html', {})

def skills_view(request):
    # Your logic here
    return render(request, 'skills.html', {})

