from django.core.management.base import BaseCommand
from django.utils import timezone
from recommend_app.scripts import scrap_pilot
class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        scrap_pilot.count_run_check()
        self.stdout.write("Populated")