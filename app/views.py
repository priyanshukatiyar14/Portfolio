from django.shortcuts import render
from .models import AboutMe, Skill, Project, Experience,Contact
from .forms import ContactForm
from django.shortcuts import redirect

def home(request):
    about_me = AboutMe.objects.first()
    skills = Skill.objects.all()
    projects_model_obj = Project.objects.all()
    projects=[]
    for project in projects_model_obj:
        skill_arr=""
        for skill in project.skills.all():
            skill_arr+=skill.name+", "
        project_obj = {
            'title': project.title,
            'description': project.description,
            'image': project.image,
            'link': project.link,
            'skills': skill_arr[:-2]
        }
        projects.append(project_obj)

    experiences = Experience.objects.all()
    for experience in experiences:
        if experience.end_date is None:
            experience.end_date = 'Present'
        if experience.description:
            experience.description = experience.description.split('#')
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

from django.views.decorators.csrf import csrf_exempt


def contact_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        Contact.objects.create(name=name, email=email, phone=phone, message=message)
        
        return redirect('/#contact') # Redirect to a new URL for success message or back to form
    return render(request, 'index.html') 

