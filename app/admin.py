from django.contrib import admin
from .models import AboutMe, Skill, Project, Experience, Contact

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')  # Customize as needed
    filter_horizontal = ('skills',)  # This makes selecting skills easier

admin.site.register(AboutMe)
admin.site.register(Skill)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Experience)
admin.site.register(Contact)

admin.site.site_header = "Priyanshu's Portfolio Admin Panel"
admin.site.site_title = "Priyanshu's Portfolio Admin Panel"
admin.site.index_title = "Welcome to Priyanshu's Portfolio Admin Panel"