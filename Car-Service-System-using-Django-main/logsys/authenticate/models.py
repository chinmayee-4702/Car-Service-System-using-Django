from email.policy import default
from django.db import models

# Create your models here.
class Contact(models.Model):
    message = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=150,default="")
    lastname = models.CharField(max_length=150,default="")
    email = models.CharField(max_length=150,default="")
    #num = models.CharField(max_length=15,default="")
    message = models.TextField(max_length=500,default="")
    city=models.CharField(max_length=100,default="")

    def _str_(self) :
        return self.name

class Appoint(models.Model):
    # appointname = models.AutoField(primary_key=True)
    # appointname=models.CharField(max_length=150,default="")
    appointemail = models.CharField(max_length=150,default="")
    # appointtime=models.CharField(max_length=150,default="")
    appointdate = models.CharField(max_length=150,default="")
    appointmentfor = models.CharField(max_length=150,default="")
    def _str_(self) :
        return self.name

# class Feedback(models.Model):
#     feedback=models.CharField(max_length=150,default="")
#     message = models.TextField(max_length=500,default="")
#     def _str_(self) :
#         return self.name
