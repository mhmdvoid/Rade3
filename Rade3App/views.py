from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Victim_Request,Victim_Request_Status
from .serializers import VictimRequestSerializer,VictimRequestStatusSerializer
# Create your views here.


@api_view(['GET'])
def Rade3Api (request):

    api_urls ={
        'List': '/request-list/',
        'Request Detail': '/request-detail/<str:pk>/',
        'Create Request': '/request-create/',
        'Update Request': '/request-update/<str:pk>/',
        'Delete Request': '/request-delete/<str:pk>/',
        'Request Status List': '/request-staus-list/',
        'Request Status Detail': '/request-staus-detail/<str:pk>/',
        'Update Request Status': '/request-staus-update/<str:pk>/',
    } 
    return Response(api_urls)
#Victim_Request Model
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


#Victim_Request_Status

@api_view(['GET'])
def victimRequestStatusList (request):
    requests = Victim_Request_Status.objects.all()
    serializer = VictimRequestStatusSerializer(requests, many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def victimRequestStatusDetail (request,pk):
    vrequest = Victim_Request_Status.objects.get(id=pk)
    serializer = VictimRequestStatusSerializer(vrequest, many=False)
    
    return Response(serializer.data)


@api_view(['POST'])
def victimRequestStatusUpdate(request,pk):
    vrequest = Victim_Request_Status.objects.get(victim=pk)
    serializer = VictimRequestStatusSerializer(instance=vrequest, data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
