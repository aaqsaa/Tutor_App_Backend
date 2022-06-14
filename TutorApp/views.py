from os import stat
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CodeEditorSerializer,OrderRequestSerializer,OrderStatusChangeSerializer
from .models import CodeEditor,OrderRequest





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


@api_view(['GET','PUT'])
def request_teacher_order_details(request,teacher_id):
    if request.method=='GET':
        try:
            requested=OrderRequest.objects.filter(teacher_id=teacher_id)
        except OrderRequest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=OrderRequestSerializer(requested,many=True)
        listData=[]
        for x in requested:
            data={}
            print("student name: ",x.student.fullname)
            print("student price: ",x.price)
            data["name"]=x.student.fullname
            data["id"]=x.id
            data["description"]=x.description
            data["price"]=x.price
            data["files"]=x.files
            data["date"]=x.date
            data["status"]=x.status
            data["teacher_id"]=x.teacher_id
            data["student_id"]=x.student_id
            listData.append(data)
        print("specific reviews are---",serializer.data)
        print("List Data: ",listData)
        return Response(listData)


@api_view(['GET','PUT'])
def order_status_change(request,order_id):
    if request.method=='PUT':
        requested=OrderRequest.objects.get(id=order_id)
        serializer = OrderStatusChangeSerializer(requested,data=request.data) 
        print("The Requested Data is: ",request.data)
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


def front(request):
    context = { }
    return render(request, "index.html", context)
