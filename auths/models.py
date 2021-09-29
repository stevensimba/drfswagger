from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import (
  BaseUserManager, AbstractBaseUser
)

# Create your models here.

class NewUserManager(BaseUserManager):
      def create_user(self, email, password=None, **extra_fields):
            extra_fields.setdefault('is_superuser', False)
            if not email:
                  raise ValueError("Users must have an email address")

            user = self.model(email=self.normalize_email(email), **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user  
      
      def create_manager(self, email, password, **extra_fields):
          user = self.create_user(email= self.normalize_email(email), password=password, **extra_fields)
          user.manager = True 
          user.save(using=self._db)
          return user 

      def create_superuser(self, email, password, **extra_fields):
            extra_fields.setdefault('is_superuser', True)
            extra_fields.setdefault('is_staff', True)
            extra_fields.setdefault('is_admin', True)
            return self.create_user(email=self.normalize_email(email), password=password, **extra_fields)
         

class NewUser(AbstractBaseUser, PermissionsMixin):
    # add fields and modify: id, password, last_login, is_superuser, email
      email = models.EmailField(   verbose_name="email address",max_length=255,   unique=True )
      date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
      first_name = models.CharField(verbose_name="first name", max_length=30, null=False)
      # blank is for fields and null is for database 
      last_name = models.CharField(verbose_name="last name", max_length=30, null=False)
      is_manager = models.BooleanField(default=False)
      avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)

      # admin/  requires is_staff and is_admin 
      is_staff= models.BooleanField(default=False)
      is_admin = models.BooleanField(default=False)

      #unique field change from username to email
      USERNAME_FIELD='email'
      REQUIRED_FIELDS = [ "password", "first_name", "last_name"]
      
      objects = NewUserManager()

      class Meta:
            verbose_name = "newuser"
            verbose_name_plural = "newusers"

      def get_full_name(self):
            return f"{self.first_name} {self.last_name}"

      def get_short_name(self):
            return  f"{self.last_name}"

      def __iter__(self):
            field_names = [f.name for f in self._meta.fields]
            for field_name in field_names:
                  value = getattr(self, field_name, None)
                  yield (field_name, value)

      """
      __iter__(self): usage 

      obj = iter(User.objects.get(id=1))
      try:
            while True:
                  print("(field, value)", next(obj))
      except:
            print("END!!!")
      """

# >>> User._meta.get_fields()