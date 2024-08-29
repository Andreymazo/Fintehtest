from django.core.management import BaseCommand
from django.contrib.auth.models import User
# from catalog.models import CustomUser


# from users.models import CustomUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            username='andreymazo',
            is_staff=True
        )
        user.set_password('qwert123asd')
        user.is_superuser = True

        user.save()
#         {"username": "andreymazo@mail.ru",
# "password":"qwert123asd"}
