from django.db import models

class Usuario (models.Model):
    # no getters and setters please (http://dirtsimple.org/2004/12/python-is-not-java.html)

    registro     = models.PositiveIntegerField()
    nome         = models.CharField(max_length=200)
    departamento = models.CharField(max_length=200)
    estado       = models.PositiveSmallIntegerField()
    tipo_perfil  = models.PositiveSmallIntegerField()
    email        = models.EmailField()

    class Meta:
        db_table = 'Usuarios'
        app_label = 'app'
