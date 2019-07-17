from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission


class Command(BaseCommand):

    def handle(self, *args, **options):
        username = input('Введите имя пользователя: ')
        password = input('Введите пароль: ')

        if User.objects.filter(username=username).count() == 0:
            user = User.objects.create(username=username, password=password, is_superuser=True, is_staff=True)
            permission = Permission.objects.all()
            for p in permission:
                user.user_permissions.add(p)
        else:
            print('Такой пользователь уже есть')
