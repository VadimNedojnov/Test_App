from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


from account.models import User
from logger.models import LogCreatedEditedDeleted


@receiver(post_save, sender=User)
def model_created_edited(sender, instance, **kwargs):
    LogCreatedEditedDeleted.objects.create(
        message=f' Action: change or create object {instance}')


@receiver(post_delete)
def model_deleted(sender, instance, **kwargs):
    LogCreatedEditedDeleted.objects.create(
        message=f' Action: delete object {instance}')
