from django.urls import path
from . import views

urlpatterns = [
    path("enroll/", views.enroll_student, name="enroll_student"),
    path("courses/", views.course_list, name="course_list"),
]
