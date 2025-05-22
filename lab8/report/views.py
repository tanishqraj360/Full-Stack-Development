from django.shortcuts import render
import csv
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table
from .models import Student

# Create your views here.


def student_report_options(request):
    return render(request, "report/student_report_options.html")


def generate_student_csv(request):
    students = Student.objects.all()
    model_fields = ["name", "usn", "email", "major"]

    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="students.csv"'

    writer = csv.writer(response)
    writer.writerow([field.upper() for field in model_fields])

    for student in students:
        row = [getattr(student, field) for field in model_fields]
        writer.writerow(row)

    return response


def generate_student_pdf(request):
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="students.pdf"'

    doc = SimpleDocTemplate(response, pagesize=letter)
    story = []

    data = [["NAME", "USN", "EMAIL", "MAJOR"]]
    students = Student.objects.all()
    for student in students:
        data.append([student.name, student.usn, student.email, student.major])

    table = Table(data)
    story.append(table)

    doc.build(story)
    return response
