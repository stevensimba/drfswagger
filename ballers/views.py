from typing import List
from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from . import models 
from . import serializers
from rest_framework import permissions 

# Create your views here.

class SampleBallers(ListAPIView):
      serializer_class = serializers.BallerSerializer
      permission_classes = (permissions.AllowAny, )
    

      def get_queryset(self):
            return models.Baller.objects.all()[:3]


class BallerList(ListCreateAPIView):
     serializer_class = serializers.BallerSerializer
     permission_classes = (permissions.IsAuthenticated, )

     def perform_create(self, serialize):
           serialize.save(owner = self.request.user)

     def get_queryset(self):
          return models.Baller.objects.order_by("date_entry")[:10]

class BallerDetail(RetrieveUpdateDestroyAPIView):
      serializer_class = serializers.BallerSerializer 
      permission_classes = (permissions.IsAuthenticated, )
      lookup_field = "id"

      def get_queryset(self):
            return models.Baller.objects.filter(owner=self.request.user) 

           

