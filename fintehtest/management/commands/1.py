from django.core.management import BaseCommand
from config.settings import BASE_DIR, STATICFILES_DIRS
from fintehtest.models import Item



def ff():
   print(BASE_DIR, '/', STATICFILES_DIRS)#, STATIC_FILES_DIRS)
    # Item.objects.create(name = "boat",
    # description = "verywell boat",
    # price=112)
class Command(BaseCommand):

    def handle(self, *args, **options):
        ff()

