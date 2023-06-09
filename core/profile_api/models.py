from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin, BaseUserManager


# Create your models here.
class UserProfileManager(BaseUserManager):
    """ manager for user profile"""

    def create_user(self, email, name, password=None):
        """create a new user profile"""
        if not email:
            raise ValueError("email must not be empty")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    
    def create_superuser(self, email, name, password):
        """create a new superuser"""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Data model for user profile in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    if_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    
    objects = UserProfileManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    def get_full_name(self):
        """Retreive the full name of the user"""
        return self.name
    
    def get_short_name(self):
        """Retreive the short name of the user"""
        return self.name
    
    
    def __str__(self):
        """Return a string representation of the user"""
        return self.email