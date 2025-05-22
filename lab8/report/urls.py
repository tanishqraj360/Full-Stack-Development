# report_generator/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("generate_csv/", views.generate_student_csv, name="generate_student_csv"),
    path("generate_pdf/", views.generate_student_pdf, name="generate_student_pdf"),
    path("", views.student_report_options, name="student_report_options"),
]
