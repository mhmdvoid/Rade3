from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


@api_view(['GET'])
def Rade3Api (request):

    api_urls ={
        'Requests': '/reqeusts-list/',
        'Request Detail': '/request-detail/<str:pk>',
        'Create Request': '/request-create/',
        'Update Request': '/request-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    } 
    return Response(api_urls)
