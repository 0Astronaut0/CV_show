from django.db import models

class inp_data(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=11,blank=True)
    summary = models.TextField()
    skills = models.TextField()
    exprience = models.TextField()
    education = models.TextField()

