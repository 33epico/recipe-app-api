from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                                PermissionsMixin

#Manejador del modelo de usuario
class UserManager (BaseUserManager):

    def create_user(self , email, password = None, **extra_fields):
        """Crea y salva un nuevo usuario"""
        if not email:
            raise ValueError('Es imprescindible poner un email')
        user = self.model(email = self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self , email, password):
        """Funcion para crear un super usuario, no se pone extra_fields por """
        user = self.create_user(email,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
        """Modelo de usuario propio con soporte del email en vez de nombre de usuario"""
        email = models.EmailField (max_length = 255,unique = True)
        name = models.CharField (max_length = 255)
        is_active = models.BooleanField (default = True)
        is_staff = models.BooleanField (default =False)

        
        #esto establece el manejador del modelo de usuario, que es la clase de arriba
        objects = UserManager()

        #Esto es lo que django utilizará para reconocer al usuario en la autentificación
        USERNAME_FIELD = 'email'




    