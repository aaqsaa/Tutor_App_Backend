"""TutorApplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include,path
from TutorApp.views import front,CodeEditorView,request_teacher_order_details


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", front, name="front"),
    path('CodeEditor/',CodeEditorView,name="CodeEditorView"),
    path("request_teacher_details/<int:teacher_id>/",request_teacher_order_details,name="request_teacher_order_details"),
  
]
