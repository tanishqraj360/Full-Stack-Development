from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Student


# Create your views here.
#
class StudentListView(ListView):
    model = Student
    template_name = "students/student_list.html"
    context_object_name = "students"


class StudentDetailView(DetailView):
    model = Student
    template_name = "students/student_detail.html"
    context_object_name = "student"
