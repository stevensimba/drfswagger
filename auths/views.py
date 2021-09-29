from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.generics import GenericAPIView 
from .serializers import LoginSerializer, UserSerializer
from rest_framework.response import Response 
from rest_framework import status 
from django.conf import settings 
from django.contrib import auth
from rest_framework import permissions
import jwt 

# Create your views here.

def ApiMap(request):
    text = f"""
                    <h1> Api access points </h1> 
                    <p> &nbsp; &nbsp;  http://127.0.0.1/api/ballers/ </p> 
                    <p>  &nbsp; &nbsp; http://127.0.0.1/api/ballers/id/ </p> 
                 """ 
    return HttpResponse(text)
    

class RegisterView(GenericAPIView):
    serializer_class = UserSerializer
    #permission_classes = (permissions.AllowAny,)

    #overrides GenericAPIView method: post, get, put, delete
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():    #runs validate()
            serializer.save()        #runs create()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    # serializer_class presents a form with all fields specified in Meta 
    serializer_class = LoginSerializer
    #permission_classes = (permissions.AllowAny,)
    def post(self, request):
        data = request.data 
        email = data.get("email", "")
        password = data.get("password", '')
        user = auth.authenticate(email=email, password=password) 
        
        if user:
            auth_token = jwt.encode({"email": user.email}, settings.JWT_SECRET_KEY)
             # serialize: convert  an object instance into json fields 
            serializer = UserSerializer(user, many=False) 
            data = {
                "user": serializer.data, "token": auth_token
            }
            return Response(data, status=status.HTTP_200_OK)
    
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

       