from django.contrib import admin
from django.urls import path

from day01 import views

app_name = "day01"
urlpatterns = [
    # path("user/",views.user),
    # path("users/",views.UserView.as_view()),
    # path("users/<str:pk>/",views.UserView.as_view()),

    path("students/",views.StudentView.as_view()),
    path("students/<str:pk>/",views.StudentView.as_view()),

    path("2students/", views.StudentView2.as_view()),
    path("2students/<str:id>/", views.StudentView2.as_view()),
]
