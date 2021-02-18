from django.db import models

# Create your models here.
class Victim_Info (models.Model):

    name = models.CharField(max_length=200)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    email = models.EmailField(max_length=254)
    description = models.TextField()
    program = models.TextField()
    files = models.ImageField(null = True)

    blackmailer_name = models.CharField(max_length=200, null=True, blank=True)
    blackmailer_email = models.EmailField(max_length=254 , null=True, blank=True)
    blackmailer_account = models.CharField(max_length=200, null=True, blank=True)


  
    def __str__(self):
        return self.name

class Victim_Request_Status(models.Model):
    
    vid =  models.TextField()
    create_date = models.DateField(auto_now=False, auto_now_add=True)
    approved = models.BooleanField(null=True)
    completed = models.BooleanField()
    reviewr_name = models.CharField(max_length=200)

    def __str__(self):
        return self.completed

class Reviewr_Action (models.Model):
    
    vid =  models.TextField()
    create_date = models.DateField(auto_now=False, auto_now_add=True)
    description = models.TextField()
    reviewr_name  = models.CharField(max_length=200)

    def __str__(self):
        return self.description


class Resources(models.Model):
        
    name = models.TextField()
    url = models.URLField(max_length=200)
    source = models.TextField()

    def __str__(self):
        return self.name