from django.shortcuts import redirect, render
from .models import Project
from .forms import ProjectForm


# Create your views here.
#
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("project_list")
    else:
        form = ProjectForm()
    return render(request, "projects/create_project.html", {"form": form})


def project_list(request):
    projects = Project.objects.all()
    return render(request, "projects/project_list.html", {"projects": projects})
