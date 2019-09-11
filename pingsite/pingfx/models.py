from django.db import models

# Create your models here.

class Websites(models.Model):
    URL = models.CharField(max_length=200)
    def __str__(self):
        return self.URL

class Users(models.Model):
    user = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    def __str__(self):
        return self.user
