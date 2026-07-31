from django.core.management import BaseCommand

from account.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user, created = User.objects.get_or_create(
            email='admin@admin.com',
            defaults={
                'is_superuser': True,
                'is_staff': True
            }
        )
        user.set_password('admin')
        user.save()

        if created:
            self.stdout.write(self.style.SUCCESS(f'Создан superuser {user.email}'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Пользователь superuser {user.email} уже существует'))