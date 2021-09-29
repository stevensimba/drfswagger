"""contactsapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include 

from rest_framework import permissions 

# Api user interface 
from drf_yasg.views import get_schema_view 
from drf_yasg import openapi 

schema_view = get_schema_view(
    openapi.Info(
        title="Ballers API", 
        default_version = "v1", 
        description="An API about Football players in 3 simple steps.  \n 1. shows a sample of current footballers in our databases \n 2. To see more players and submit more players,  register as a user.  \n 3. The registration username and password are used to login, and a token is issued \n 4. The token when presented in the header as [Bearer xx] give access to the players  information. \n  \n The logged in user can read, write, update and delete players", 
        terms_of_service="https://stevensimba.github.io", 
        contact=openapi.Contact(email="sigsimba@gmail.com"),
        license=openapi.License(name="BSD License"), 
    ), 
    public=True, 
    permission_classes = (permissions.AllowAny, ), 
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # the auths app issue a bearer token to be used to access ballers fields
    path('api/ballers/', include('ballers.urls')),
    path('api/', include('auths.urls')),
    # path("api", include("auths.urls"))  # api or api/ 

    path(r"", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger'), 
     path(r"redoc/", schema_view.with_ui('redoc', cache_timeout=0), name='doc-swagger'), 
]
