from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Victim_Request (models.Model):
    
    name = models.CharField(max_length=200)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    email = models.EmailField(max_length=254) 
    description = models.TextField() 

    program = models.TextField() 

    files = models.ImageField(null = True) 

    blackmailer_name = models.CharField(max_length=200)
    blackmailer_email = models.EmailField(max_length=254)
    blackmailer_account = models.CharField(max_length=200)

  
    def __str__(self):
        return self.name

@receiver(post_save, sender = Victim_Request)
def create_victim_request_status(sender, instance, created, **kwargs):
    if created:
        Victim_Request_Status.objects.create(victim=instance)
        print('created')

post_save.connect(create_victim_request_status, sender=Victim_Request)

class Victim_Request_Status(models.Model):
    
    create_date = models.DateField(auto_now=False, auto_now_add=True) 
    approved = models.BooleanField(default=False)
    contact_blackmailer = models.BooleanField(default=False)
    timeـout = models.BooleanField(default=False)
    results = models.TextField(null = True) 
 
    victim = models.OneToOneField(Victim_Request,on_delete=models.CASCADE)
     




class Resources(models.Model):
        
    name = models.TextField()
    url = models.URLField(max_length=200)
    source = models.TextField()

    def __str__(self):
        return self.name