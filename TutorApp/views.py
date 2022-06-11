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

@api_view(['GET','POST'])
def Compiler(request):
    print('in compiler')
    if request.method=='GET':
        
        return Response(status=status.HTTP_201_CREATED)
    if request.method=='POST':
        print('in Compiler API')
        code =  request.data.code
        language=request.data.language
        input1=request.data.input
        data = {
        "code": code,
        "language": language,
        "input": input1
        }
        config = {
            method: 'post',
            url: 'https://codexweb.netlify.app/.netlify/functions/enforceCode',
            headers: {
                'Content-Type': 'application/json'
            },
            data: data
        }
        


def front(request):
    context = { }
    return render(request, "index.html", context)
