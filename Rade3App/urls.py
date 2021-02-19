from django.urls import path
from . import views

urlpatterns = [
path ('',views.Rade3Api, name="Rade3Api"),
path ('request-list/',views.victimRequestList, name="request-list"),
path ('request-detail/<str:pk>/',views.victimRequestDetail, name="request-detail"),
path ('request-create/',views.victimRequestCreate, name="request-create"),
path ('request-update/<str:pk>/',views.victimRequestUpdate, name="request-update"),
path ('request-delete/<str:pk>/',views.victimRequestDelete, name="request-delete"),
path ('request-staus-list/',views.victimRequestStatusList, name="request-staus-list"),
path ('request-staus-detail/<str:pk>/',views.victimRequestStatusDetail, name="request-staus-detail"),
path ('request-staus-update/<str:pk>/',views.victimRequestStatusUpdate, name="request-staus-update"),
]
