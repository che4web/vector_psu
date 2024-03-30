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
from django.urls import path,include
from programapp.views import (program_list,
                              program_detail,
                              program_list_json,
                              SpecialityListView,
                              program_create,
                              ProgramViewSet,
                              ProgramCreateView,
                              SpecialityViewSet
                              )
from courseapp.views import CourseListView,CourseDetailView,CourseViewSet
from helperapp.views import InterestViewSet

from rest_framework.routers import DefaultRouter

from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'program', ProgramViewSet, basename='program')
router.register(r'course', CourseViewSet, basename='course')
router.register(r'speciality', SpecialityViewSet, basename='speciality')
router.register(r'interest', InterestViewSet, basename='interest')

urlpatterns = [
    path("",program_list),
    path("program/json/",program_list_json),
    path("program/create",ProgramCreateView.as_view()),
    #path("program/create",program_create),
    path("program/<int:pk>/",program_detail),
    path("course/",CourseListView.as_view()),
    path("course/<int:pk>/",CourseDetailView.as_view()),
    path("speciality/",SpecialityListView.as_view()),
    path('admin/', admin.site.urls),
    path('api/',include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
