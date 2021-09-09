from django.db import models


class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=122)
    phone=models.CharField(max_length=13)
    email=models.CharField(max_length=112)
    content=models.TextField()
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.name

# Create your models here.
