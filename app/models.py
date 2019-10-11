from django.conf import settings
from django.db import models


class SettingPlanner(models.Model):
    size = models.CharField(max_length=2)
    leaf = models.CharField(max_length=15)
    ear = models.CharField(max_length=4)

    def save_setting(self):
        self.save()

    def __str__(self):
        return self.size
