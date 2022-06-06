from django.db import models

# Create your models here.
class Contact(models.Model):
    message = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=150,default="")
    lastname = models.CharField(max_length=150,default="")
    email = models.CharField(max_length=150,default="")
    #num = models.CharField(max_length=15,default="")
    message = models.TextField(max_length=500,default="")

    def _str_(self) :
        return self.name