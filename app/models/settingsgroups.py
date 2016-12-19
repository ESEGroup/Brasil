from django.db import models

#primary keys

class SettingsUserGroups(models.Model):
    SuperAdminGroup = 1
    AdminGroup = 2
    FuncGroup = 3