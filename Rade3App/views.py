from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Victim_Request 
from .serializers import VictimRequestSerializer
# Create your views here.


@api_view(['GET'])
def Rade3Api (request):

    api_urls ={
        'List': '/request-list/',
        'Request Detail': '/request-detail/<str:pk>/',
        'Create Request': '/request-create/',
        'Update Request': '/request-update/<str:pk>/',
        'Delete': '/request-delete/<str:pk>/',
    } 
    return Response(api_urls)

@api_view(['GET'])
def victimRequestList (request):
    requests = Victim_Request.objects.all()
    serializer = VictimRequestSerializer(requests, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def victimRequestDetail (request,pk):
    vrequest = Victim_Request.objects.get(id=pk)
    serializer = VictimRequestSerializer(vrequest, many=False)
    
    return Response(serializer.data)


@api_view(['POST'])
def victimRequestCreate (request):
   
    serializer = VictimRequestSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def victimRequestUpdate(request,pk):
    vrequest = Victim_Request.objects.get(id=pk)
    serializer = VictimRequestSerializer(instance=vrequest, data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def victimRequestDelete(request,pk):
    vrequest = Victim_Request.objects.get(id=pk)
    vrequest.delete();
    return Response('Item successfully delete!')