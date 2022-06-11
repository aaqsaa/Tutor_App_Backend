from os import stat
from pickle import GET
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import  ReviewSerializer, PackageSerializer,StudentOrderSerializer, OrderRequestSerializer, GigsSerializer,TeachersSerializer,TeacherOrderSerializer
from .models import Gigs,GigRating, Orders,Teachers,OrderRequest,Reviews, GigPackages
import base64
from PIL import Image
import io 




# Create your views here.

#Getting Gigs
@api_view(['GET','POST'])
def Gig(request):
  
    if request.method=='GET':
        Gig=Gigs.objects.all() 
        print("Tempppppppppppp: ",Gig[0].teacher.fullname)
        serializer=GigsSerializer(Gig,many=True)

        print("checking...",serializer.data[0]["name"])
        images=[]
        ratings=[]
        names=[]
        teacher_images=[]

        teachers={}
        for gig in Gig:
            images.append(gig.image.decode("UTF-8"))
            names.append(gig.teacher.fullname)
            teacher_images.append(gig.teacher.image)
            try: 
                rating=GigRating.objects.get(gig_id=gig.id)
                ratings.append(rating.rating)
            except GigRating.DoesNotExist:
                rating="No rating yet"
                ratings.append(rating)

        teachers={'names':names,'teacher_images':teacher_images}

        print("teacherss idct: ",teachers['teacher_images'])
        data=[serializer.data,images,ratings,teachers]
        return Response(data)
    if request.method=='POST':
         serializer = GigsSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#----------------------------- REVIEWS ----------------------------------------

@api_view(['GET','POST'])
def Review(request):
    if request.method=='GET':
        Review=Reviews.objects.all() 
        serializer=ReviewSerializer(Review,many=True)
        list=[]
        for d in Review:
            data={}
            data["name"]=d.student.fullname
            data["email"]=d.student.email
            data["image"]=d.student.image
            data["rating"]=d.rating
            data["text"]=d.text
            list.append(data)
        return Response(list)
    if request.method=='POST':
         serializer = ReviewSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])        
def Review_details(request,gig_id):
    if request.method=='GET':
        try:
            review=Reviews.objects.filter(gig_id=gig_id)
        except Reviews.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=ReviewSerializer(review,many=True)
        
        list=[]
        for d in review:
            data={}
            data["name"]=d.student.fullname
            data["email"]=d.student.email
            data["image"]=d.student.image
            data["rating"]=d.rating
            data["text"]=d.text
            list.append(data)
        return Response(list) 


@api_view(['DELETE'])
def Review_delete(request,pk):
    try:
        review=Reviews.objects.get(pk=pk)
    except Reviews.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 


#-------------------------------PACKAGES-------------------------------


@api_view(['GET','POST'])
def Package(request):
    if request.method=='GET':
        Package=GigPackages.objects.all() 
        serializer=PackageSerializer(Package,many=True)
        list=[]
        for d in Package:
            data={}
            data["name"]=d.package.name
            data["services"]=d.package.services
            data["type"]=d.package.type
            data["price"]=d.package.price
            list.append(data)
        return Response(list)
    if request.method=='POST':
         serializer = PackageSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])        
def Package_details(request,gig_id):
    if request.method=='GET':
        try:
            package=GigPackages.objects.filter(gig_id=gig_id)
        except GigPackages.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=PackageSerializer(package,many=True)
        list=[]
        for d in package:
            data={}
            data["name"]=d.package.name
            data["services"]=d.package.services
            data["type"]=d.package.type
            data["price"]=d.package.price
            list.append(data)
        return Response(list) 


@api_view(['DELETE'])
def Package_delete(request,gig_id):
    try:
        package=GigPackages.objects.get(gig_id=gig_id)
    except GigPackages.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='DELETE':
        package.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#-------------------------Order----------------------------


@api_view(['GET','POST'])
def Order(request):
    if request.method=='GET':
        Order=Orders.objects.all()
        serializer=StudentOrderSerializer(Order,many=True)
        print("data from review table",serializer.data)
        return Response(serializer.data)
    if request.method=="POST":
        serializer =StudentOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#--- get specified record of Student---
@api_view(['GET'])
def order_details(request,student_id):
    if request.method=='GET':
        try:
            order=Orders.objects.filter(student_id=student_id)
        except Orders.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=StudentOrderSerializer(order,many=True)
        print("specific reviews are---",serializer.data)
        return Response(serializer.data)

#--- get specified record of Teacher---

@api_view(['GET'])
def teacher_order_details(request,teacher_id):
    if request.method=='GET':
        try:
            order=Orders.objects.filter(teacher=teacher_id)
        except Orders.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=TeacherOrderSerializer(order,many=True)
        print("specific reviews are---",serializer.data)
        return Response(serializer.data)

# ---delete record---
@api_view(['DELETE'])
def order_delete(request,pk):
    try:
        order=Orders.objects.get(pk=pk)
    except Orders.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#---------------------------Order Requests---------------------------------

@api_view(['GET','POST'])
def Request(request):
    if request.method=='GET':
        Request=OrderRequest.objects.all()
        serializer=StudentOrderSerializer(Request,many=True)
        print("data from review table",serializer.data)
        return Response(serializer.data)
    if request.method=="POST":
        serializer =StudentOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#--- get specified record---
@api_view(['GET'])
def request_details(request,student_id):
    if request.method=='GET':
        try:
            request=OrderRequest.objects.filter(student_id=student_id)
        except Orders.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=OrderRequestSerializer(request,many=True)
        print("specific reviews are---",serializer.data)
        return Response(serializer.data)



# ---delete record---
@api_view(['DELETE'])
def request_delete(request,pk):
    try:
        request=OrderRequest.objects.get(pk=pk)
    except OrderRequest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='DELETE':
        request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




#Getting specific Teacher 
@api_view(['GET'])
def Teacher(request,id):
  
    if request.method=='GET':
        try:
            teacher=Teachers.objects.get(id=id) 
        except Teachers.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer=TeachersSerializer(teacher)
        data=[serializer.data]
        print("_____________________data____________________: ",data)
        return Response(data)


# def TeacherProfileData1(teacher_id):
  
#         teacher=Teachers.objects.get(id=teacher_id) 
#         # serializer=TeachersSerializer(teacher)
#         data=[teacher]
#         print("_____________________data____________________: ",data)
# TeacherProfileData1(1)

@api_view(['DELETE'])
def Gig_detail(request,pk):
    try:
        gig=Gigs.objects.get(pk=pk)
    except Gigs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='DELETE':
        gig.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






def front(request):
    context = { }
    return render(request, "index.html", context)
