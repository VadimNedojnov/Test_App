from django.db import models


from logger import model_choices as mch


class Logger(models.Model):
    path = models.CharField(max_length=128)
    method = models.PositiveIntegerField(choices=mch.METHOD_CHOICES)
    time_delta = models.DecimalField(max_digits=5, decimal_places=3)
    user_id = models.IntegerField(null=True, blank=True)
    user_name = models.CharField(max_length=20, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
