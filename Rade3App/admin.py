from django.contrib import admin
from .models import Victim_Request ,Victim_Request_Status, Resources
# Register your models here.



admin.site.register(Victim_Request )
admin.site.register(Victim_Request_Status)
admin.site.register(Resources)