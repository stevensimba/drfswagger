from django.urls import path 
from . import views 

urlpatterns = [
    path("", views.ApiMap, name="api-map"),
    path('register/', views.RegisterView.as_view(), name='register'), 
    path('login/', views.LoginView.as_view(), name='login'),
]