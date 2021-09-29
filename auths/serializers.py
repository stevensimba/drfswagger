from rest_framework import serializers
#from django.contrib.auth.models import User
from auths.models import NewUser 

# Serializers validate input fields
class UserSerializer(serializers.ModelSerializer):
    # all the fields must come from an existing model e.g. User 
    # Fields to show, must be required=True, either in serializer or model
   # username = serializers.CharField(max_length=25, min_length=2)
    first_name =  serializers.CharField(max_length=255, min_length=2, required=True)
    last_name  = serializers.CharField(max_length=255, min_length=2, required=True)
    email = serializers.EmailField(max_length=255, min_length=4, required=True )
    # write_only=True: inputs must not be returned 
    password = serializers.CharField(max_length=65, min_length=6, write_only=True) 

    class Meta:
        model =NewUser              
        #fetch user model  fields, fields  required=True are shown to the user
        fields = [ 'first_name', 'last_name', 'email', 'password']

    #overrides internal validate  and create methods 
    def validate(self, attrs):
        email = attrs.get('email', '')
        if NewUser.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email":("Email is already in use.")})
        return super().validate(attrs)   #run the default validate method 

    #saving the user data    
    def create(self, validated_data):
        #return super().create(validated_data)
        return NewUser.objects.create_user(**validated_data) 
        #without: ** (it puts all values in first field)  : *args, **kwargs



class LoginSerializer(serializers.ModelSerializer):
        email = serializers.CharField(max_length=25, min_length=2)
        password = serializers.CharField(max_length=65, min_length=6, write_only=True) 

        class Meta:
            model = NewUser 
            fields = ['email', 'password']
