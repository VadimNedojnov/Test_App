# Generated by Django 2.2.10 on 2020-04-14 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0003_logcreatedediteddeleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logcreatedediteddeleted',
            name='user_name',
        ),
    ]