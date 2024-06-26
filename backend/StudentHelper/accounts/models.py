from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    year = models.CharField(max_length=10)  # Assuming year is a string field, change it accordingly
    sector = models.CharField(max_length=255, blank=True)  
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

# class Chat(models.Model):
#     sender = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
#     timeStamp = models.DateTimeField(auto_now = True)
#     content = models.CharField(max_length=10000)

# class Conversation(models.Model):
#     message = models.ForeignKey(Chat, on_delete=models.CASCADE)

