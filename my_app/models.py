from django.db import models


# Create your models here.
class Contact(models.Model):
    firstname = models.CharField(max_length=50, default="")
    lastname = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.firstname
