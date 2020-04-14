from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType


class Command(BaseCommand):
    help = 'This command shows all models and object counts'

    def handle(self, *args, **options):
        models = ContentType.objects.all()

        return ''.join(f'Model name: {i}, objects count: '
                       f'{i.get_all_objects_for_this_type().count()} \n' for i in models)
