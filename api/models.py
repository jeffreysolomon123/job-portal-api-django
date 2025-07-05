from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class JobPost(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.IntegerField()
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class Applicant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    resume_link = models.URLField()
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)
