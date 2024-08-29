from django.core.management import BaseCommand
from config.settings import BASE_DIR
from fintehtest.models import Item



def ff():
    Item.objects.create(name = "boat",
    description = "verywell boat",
    price=112)
class Command(BaseCommand):

    def handle(self, *args, **options):
        ff()

