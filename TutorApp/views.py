from os import stat
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import GigsSerializer
from .models import Gigs
import base64
from PIL import Image
import io 




# Create your views here.
@api_view(['GET','POST'])
def Gig(request):
  
    # request.method='POST'
    if request.method=='GET':
        Gig=Gigs.objects.all() 
        serializer=GigsSerializer(Gig,many=True)
        print("Image position: ",Gig[0].image.decode('UTF-8'))
        images=[]
        for gig in Gig:
            images.append(gig.image.decode("UTF-8"))
        print("Images list: ",images)
        # image_data = base64.b64encode(Gig[2].image).decode()
        data=[serializer.data,images]
        print("Final data Type:___________________ ",data)
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





# @api_view(['GET','POST'])
# def Dummy(request):
#     # request.method='POST'
#     if request.method=='GET':
#         Demoo=demo.objects.all()
#         serializer=DemoSerializer(Demoo,many=True)
#         return HttpResponse(serializer.data)
#     if request.method=='POST':
#          serializer = DemoSerializer(data=request.data)
#          if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)
#          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     return HttpResponse("Hello method is not post nor Get")
def front(request):
    context = { }
    return render(request, "index.html", context)
