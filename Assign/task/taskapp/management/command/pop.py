from django.core.management.base import BaseCommand, CommandError
from taskapp.models import User, ActivityPeriod

class Command(BaseCommand):
    help = 'Populate data'

    def handle(self, *args, **options):
        User.objects.create()
        User.save()