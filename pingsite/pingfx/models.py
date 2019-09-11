from django.db import models

# Create your models here.

class Website(models.Model):
    URL = models.CharField(max_length=200)
    def __str__(self):
        return self.URL

class User(models.Model):
    user = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    def __str__(self):
        return self.user
