from django.db import models
from auths.models import NewUser 

# Create your models here.

class Baller(models.Model):
      owner = models.ForeignKey(to=NewUser, on_delete=models.CASCADE)
      name = models.CharField(max_length=25, null=False, blank=False)
      date_entry = models.DateTimeField(auto_now_add=True, verbose_name="date entry")
      club = models.CharField(max_length=25)
      active = models.BooleanField()
      nationality = models.CharField(max_length=25)
      avatar = models.URLField()


      def __str__(self):
            return self.name 
