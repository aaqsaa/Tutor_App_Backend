from os import stat
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import GigsSerializer,OrdersSerializer
from .models import Gigs,GigRating, Orders
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
