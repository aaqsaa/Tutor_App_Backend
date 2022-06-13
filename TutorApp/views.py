from os import stat
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CodeEditorSerializer
from .models import CodeEditor





# Create your views here.
@api_view(['GET','POST'])
def CodeEditorView(request):
    print("in code editor View")
    if request.method=='GET':
        Codeeditor=CodeEditor.objects.all()
        serializer=CodeEditorSerializer(Codeeditor,many=True)
        print('CodeEditor Data from serializer: ',serializer.data)
        return Response(serializer.data)
    if request.method=='POST':
        print('in post')
        serializer=CodeEditorSerializer(data=request.data)
        print('The data is: ',request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



def front(request):
    context = { }
    return render(request, "index.html", context)
