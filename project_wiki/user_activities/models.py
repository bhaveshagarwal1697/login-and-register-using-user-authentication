from django.db import models
from django.contrib.auth.models import User


class UserModel(models.Model):
	username= models.CharField(max_length=50,null=True)
	password= models.CharField(max_length=50,null= True)


class LoginModel(User):
    class Meta:
        ordering = ("username",)


class RegisterModel(User):
    class Meta:
        ordering = ("username",)
        
    
    # def full_name(self):
    #     return self.first_name #+ " - " + self.last_name
	
