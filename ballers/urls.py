from django.urls import path 
from .views import BallerDetail, BallerList, SampleBallers

urlpatterns = [
  path("sample/", SampleBallers.as_view(), name="sample_ballers"), 
  path("", BallerList.as_view(), name="baller_list"), 
  path("<int:id>/", BallerDetail.as_view()),
]