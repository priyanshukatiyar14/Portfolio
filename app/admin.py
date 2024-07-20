from django.contrib import admin
from .models import AboutMe, Skill, Project, Experience, Contact



admin.site.register(AboutMe)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(Contact)

admin.site.site_header = "Priyanshu's Portfolio Admin Panel"
admin.site.site_title = "Priyanshu's Portfolio Admin Panel"
admin.site.index_title = "Welcome to Priyanshu's Portfolio Admin Panel"