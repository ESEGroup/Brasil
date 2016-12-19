from django.db import models

#primary keys

class SettingsUserGroups(models.Model):
    SuperAdminGroup = 5
    AdminGroup = 6
    FuncGroup = 7