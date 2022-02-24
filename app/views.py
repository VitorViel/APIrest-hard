from django.shortcuts import render

from app.models import Todo
from app.serializers import TodoSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET','POST'])
def mostra_lista(request):
    if request.method == 'GET':
        todo = Todo.objects.all()
        serializer = TodoSerializer(todo, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def edita_apaga_lista(request,pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)