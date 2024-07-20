from django.db import models

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
    proficiency = models.IntegerField()

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
