"""
fill db
"""

from django.core.management.base import BaseCommand

from services.models import Category


class Command(BaseCommand):
    """
    class Command
    """
    def handle(self, *args, **options):
        print('creating categories')
        cat = Category.objects.create(name = 'курс')
        print(cat.name)
        cat = Category.objects.create(name = 'консультация')
        print(cat)
        print('end')
