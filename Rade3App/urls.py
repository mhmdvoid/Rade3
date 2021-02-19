from django.urls import path
from . import views

urlpatterns = [
path ('',views.Rade3Api, name="Rade3Api"),
path ('request-list/',views.victimRequestList, name="request-list"),
 path ('request-detail/<str:pk>/',views.victimRequestDetail, name="request-detail"),
 path ('request-create/',views.victimRequestCreate, name="request-create"),
 path ('request-update/<str:pk>/',views.victimRequestUpdate, name="request-update"),
 path ('request-delete/<str:pk>/',views.victimRequestDelete, name="request-delete"),
]
