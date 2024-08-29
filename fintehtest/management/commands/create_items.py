from django.core.management import BaseCommand
from config.settings import BASE_DIR
from fintehtest.models import Item



def ff():
    name_lst = ["boat1", "boat2", "boat3"]
    description_lst = ["verywell boat1","verywell boat2","verywell boat3",]
    price_lst = [1100, 2200, 3300]
    for i, ii, iii in zip(name_lst, description_lst, price_lst):
        Item.objects.create(name = i, description = ii, price=iii)
class Command(BaseCommand):

    def handle(self, *args, **options):
        ff()
