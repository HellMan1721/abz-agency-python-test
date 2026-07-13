from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    hire_date = models.DateField(verbose_name='date of hire')
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='salary')
    manager = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='subordinates',
    )

    class Meta:
        verbose_name = 'employee'
        verbose_name_plural = 'employees'

    def __str__(self):
        return self.name
