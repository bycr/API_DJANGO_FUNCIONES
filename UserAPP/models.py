from django.db import models

# Create your models here.
class Users(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserName = models.CharField(max_length=50)
    Usersurname = models.CharField(max_length=50)
    cedula = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    fecha = models.DateField(auto_now_add=True)
    

