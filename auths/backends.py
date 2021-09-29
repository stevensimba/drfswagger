import jwt 
from auths.models import NewUser
from rest_framework import authentication, exceptions
from django.conf import settings    

#Authenticate client tokens inserted in the headers of contact app urls 
class JWTAuthentication(authentication.BaseAuthentication):
    #override authenticate in BaseAuthentication class
    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)
        

        #empty post request  # Bearer Token : tokent xs2...
        if not auth_data:
            return None 
        if not " " in auth_data.decode("utf-8"):
            raise exceptions.AuthenticationFailed("Please put space between: Bearer <token>")
        prefix, token = auth_data.decode('utf-8').split(' ')
        

        try:
            #ensure the token is signed properly and the user exists 
            payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms="HS256")
            user = NewUser.objects.get(email=payload['email'])
            return (user, token)
        except jwt.DecodeError as identifier:
            raise exceptions.AuthenticationFailed("Your token is invalid, login")
        except jwt.ExpiredSignatureError as identifier:
            raise exceptions.AuthenticationFailed("Your token is expired, login")
        #return super().authenticate(request) 






