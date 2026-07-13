from datetime import date
from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from .models import Employee


class EmployeeTreeViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.ceo = Employee.objects.create(
            name='Alice',
            position='CEO',
            hire_date=date(2020, 1, 15),
            salary=Decimal('5000.00'),
        )
        cls.manager = Employee.objects.create(
            name='Bob',
            position='Manager',
            manager=cls.ceo,
            hire_date=date(2021, 3, 10),
            salary=Decimal('3500.00'),
        )
        cls.developer = Employee.objects.create(
            name='Carol',
            position='Developer',
            manager=cls.manager,
            hire_date=date(2022, 6, 1),
            salary=Decimal('2500.00'),
        )

    def test_tree_view_displays_hierarchy(self):
        response = self.client.get(reverse('tree'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Alice')
        self.assertContains(response, 'Bob')
        self.assertContains(response, 'Carol')
        self.assertContains(response, '15.01.2020')
        self.assertContains(response, '5000.00')
