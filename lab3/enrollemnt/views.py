from django.shortcuts import render, redirect

from .models import Course

from .forms import EnrollForm

# Create your views here.


def enroll_student(request):
    if request.method == "POST":
        form = EnrollForm(request.POST)
        if form.is_valid():
            student = form.cleaned_data["student"]
            course = form.cleaned_data["course"]

            course.enrolled_students.add(student)
            return redirect("course_list")
    else:
        form = EnrollForm()
    return render(request, "enrollemnt/enroll_student.html", {"form": form})


def course_list(request):
    courses = Course.objects.all()
    return render(request, "enrollemnt/course_list.html", {"courses": courses})
