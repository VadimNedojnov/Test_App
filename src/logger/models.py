from django.db import models


from logger import model_choices as mch


class Logger(models.Model):
    path = models.CharField(max_length=128)
    method = models.PositiveIntegerField(choices=mch.METHOD_CHOICES)
    time_delta = models.DecimalField(max_digits=5, decimal_places=3)
    created = models.DateTimeField(auto_now_add=True)


class IpLogger(models.Model):
    changed_id = models.IntegerField()
    user_ip = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)


class LogCreatedEditedDeleted(models.Model):
    message = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)


import logger.signals
