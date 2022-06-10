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
from TutorApp.views import Package,Gig,Teacher, Review_delete, Review_details,front,Review,Package_details,Package_delete, Order, order_details, order_delete,Request,request_delete,request_details,Gig_detail
urlpatterns = [
    path('admin/', admin.site.urls),
    # path("", front, name="front"),
    path("Gigs/",Gig,name="Gigs"),
    path("Teachers/<int:id>/",Teacher,name="Teacher"),
    path("Gigs/<int:pk>/",Gig_detail,name="Gig_detail"),
     path('Reviews/',Review, name="Review"),
    path("Review_details/<int:gig_id>/",Review_details,name="Review_details"),
    path("Review_delete/<int:pk>/",Review_delete,name="Review_delete"),
    path('Packages/',Package, name="Package"),
    path("Package_details/<int:gig_id>/",Package_details,name="Package_details"),
    path("Package_delete/<int:gig_id>/",Package_delete,name="Package_delete"),
    path('Order/',Order, name="Order"),
    path("order_details/<int:student_id>/",order_details,name="order_details"),
    path("order_delete/<int:pk>/",order_delete,name="order_delete"),
    path('Request/',Request, name="Request"),
    path("request_details/<int:student_id>/",request_details,name="request_details"),
    path("request_delete/<int:pk>/",request_delete,name="request_delete"),
  
]
