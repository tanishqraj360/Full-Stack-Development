from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    usn = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    major = models.CharField(max_length=50)

    def __str__(self):
        return self.name
