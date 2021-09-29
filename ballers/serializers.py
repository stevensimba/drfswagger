from rest_framework.serializers import ModelSerializer
from .models import Baller 

class BallerSerializer(ModelSerializer):
  class Meta:
    model = Baller 
    fields = ["id", "name", "club", "nationality", "active", "avatar"]