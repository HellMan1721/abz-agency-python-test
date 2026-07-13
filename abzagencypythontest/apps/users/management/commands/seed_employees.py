from datetime import date, timedelta

from django.core.management.base import BaseCommand
from faker import Faker

from ...models import Employee


class Command(BaseCommand):
    help = 'Seed the database with fake employees'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=20, help='Number of employees to create')

    def handle(self, *args, **options):
        count = options['count']
        fake = Faker('ru_RU')

        Employee.objects.all().delete()

        employees = []
        for index in range(count):
            employees.append(
                Employee(
                    name=fake.name(),
                    position=fake.job(),
                    hire_date=date.today() - timedelta(days=365 * (index + 1)),
                    salary=float(fake.random_int(min=2000, max=10000, step=500)),
                )
            )

        created = Employee.objects.bulk_create(employees)

        for employee in created:
            if employee.pk is None:
                continue

        for index, employee in enumerate(created):
            if index == 0:
                continue
            manager = created[index // 2]
            employee.manager = manager
            employee.save(update_fields=['manager'])

        self.stdout.write(self.style.SUCCESS(f'Successfully created {len(created)} employees'))
