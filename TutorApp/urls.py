from django.urls import path
from  TutorApp.views import front

urlpatterns = [
    path('', front, name='front'),
]