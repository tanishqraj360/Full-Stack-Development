from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Project(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    topic = models.CharField(max_length=200)
    languages_used = models.CharField(
        max_length=200, help_text="Comma-separated list of languages"
    )
    duration_weeks = models.IntegerField(help_text="Duration in weeks")

    def __str__(self):
        return f"{self.topic} by {self.student.name}"
