from django.db import models
from django.contrib.auth.models import User



# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    mobile = models.IntegerField()
    image = models.ImageField(upload_to='media/')
    faculty = models.ForeignKey(User,on_delete=models.CASCADE)


    

  