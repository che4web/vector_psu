"""
URL configuration for vector_psu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from programapp.views import program_list,program_detail,SpecialityListView
from courseapp.views import CourseListView,CourseDetailView

urlpatterns = [
    path("",program_list),
    path("program/<int:pk>/",program_detail),
    path("course/",CourseListView.as_view()),
    path("course/<int:pk>/",CourseDetailView.as_view()),
    path("speciality/",SpecialityListView.as_view()),
    path('admin/', admin.site.urls),
]
