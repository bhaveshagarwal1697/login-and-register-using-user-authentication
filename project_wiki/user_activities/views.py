from django.shortcuts import render 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import logout
from .models import RegisterModel
from .serializers import LoginSerializer,RegisterSerializer


class RegisterView(APIView):
	def post(self,request):
			print(request.body)
			serializer= RegisterSerializer(data=request.data)
			serializer.is_valid(raise_exception=True)
			#user= serializer.validated_data["user"]

			print(request.data)
			try:
				user=User.objects.get(username=request.data['username'])
				return Response({"error":"User already Exist"})
			except User.DoesNotExist:
				new_user=User.objects.create_user(username=request.data['username'],password=request.data['password'],email=request.data['email'])
				print(new_user)
			return Response({"message":"User Added Successfully"},status=200)
			

class LoginView(APIView):
	def post(self,request):
		serializer= LoginSerializer(data= request.data)
		serializer.is_valid(raise_exception=True)
		user= serializer.validated_data["user"]

		#login(request, user)
		token, created= Token.objects.get_or_create(user=user)
		print(token)
		#return Response({"LoggedIn Successfully"}, status=200)
		return Response({"token": token.key}, status=200)


class LogoutView(APIView):
	authentication_classes= (TokenAuthentication, )

	def post(self, request):
		#logout(request)
		#request.user.token.delete()
		return Response({"Message":"LoggedOut successfully"},status=204)



