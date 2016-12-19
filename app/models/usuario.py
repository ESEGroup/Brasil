from django.contrib.auth.models import User
from django.db import models

class Usuario (models.Model):
    # no getters and setters please (http://dirtsimple.org/2004/12/python-is-not-java.html)
    user         = models.OneToOneField(User, default=0, related_name='profile',on_delete=models.CASCADE)
    registro     = models.PositiveIntegerField()
    #nome         = models.CharField(max_length=200)
    departamento = models.CharField(max_length=200)
    #estado       = models.PositiveSmallIntegerField()
    #tipo_perfil  = models.PositiveSmallIntegerField()
    #email        = models.EmailField()

    def __str__(self):
        return self.user.username + ' - '+ self.user.first_name

    class Meta:
        db_table = 'Usuarios'
        app_label = 'app'
