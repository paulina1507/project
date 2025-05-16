from django.db import models

# Create your models here.
class Project(models.Model):
    title =models.CharField(max_length=200)
    description =models.TextField()
    technology =models.CharField(max_length=200)
    created_by=models.DateTimeField(auto_now_add=True)