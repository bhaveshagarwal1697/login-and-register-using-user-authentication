from rest_framework import serializers
from .models import LoginModel,RegisterModel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import exceptions

class ModSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields= '__all__'


class LoginSerializer(serializers.Serializer):
	username= serializers.CharField()
	password= serializers.CharField()


	def validate(self,data):
		username= data.get("username", "")
		password= data.get("password","")

		if username and password:
			user= authenticate(username= username, password=password)
			if user:
				if user.is_active:
					data["user"]= user
				else:
					msg= "User is offline."
					raise exceptions.ValidationError(msg)
			else:
				msg= "Invalid Username or password"
				raise exceptions.ValidationError(msg)
		else:
			msg= "Enter both Username and Password"
			raise exceptions.ValidationError(msg)
		return data

class RegisterSerializer(serializers.Serializer):
	username=serializers.CharField()
	password= serializers.CharField()
	email=serializers.EmailField()

	def validate(self,data):
		username= data.get("username", "")
		password= data.get("password","")
		email= data.get("email","")

		if username and password:
			user= authenticate(username= username, password=password)
		else:
			msg= "Enter both Username and Password"
			raise exceptions.ValidationError(msg)
		return data



