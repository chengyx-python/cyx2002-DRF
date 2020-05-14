# from django.contrib import admin
from django.urls import path

from day02 import views

app_name = "day02"
urlpatterns = [

    path("employees/", views.EmployeeAPIView.as_view()),
    path("employees/<str:id>/", views.EmployeeAPIView.as_view()),
]
