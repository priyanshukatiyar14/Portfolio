from django.db import models
from django.core.files.storage import default_storage
from django.contrib.postgres.fields import ArrayField

class AboutMe(models.Model):
    intro= models.TextField(null=True)
    description = models.TextField(null=True)
    age = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=20,null=True)
    address = models.CharField(max_length=100,null=True)
    resume_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.description[:50]

class Skill(models.Model):
    name = models.CharField(max_length=100)
    link = models.ImageField(upload_to='static/images/skills', blank=True, null=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Check if the object already exists and has an image
        if self.pk:
            try:
                old_file = Skill.objects.get(pk=self.pk).link
            except Skill.DoesNotExist:
                old_file = None

            # If there's a new file being uploaded
            if old_file and self.link and old_file != self.link:
                # Delete the old file from the filesystem
                if old_file.name and default_storage.exists(old_file.name):
                    default_storage.delete(old_file.name)

        super(Skill, self).save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        # If the Skill instance has an associated image, delete it from the filesystem
        if self.link.name and default_storage.exists(self.link.name):
            default_storage.delete(self.link.name)
        super(Skill, self).delete(*args, **kwargs)

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='static/images/projects')
    link = models.URLField(blank=True, null=True)
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.title

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name
