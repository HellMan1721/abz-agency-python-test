from django.shortcuts import render

from .apps.users.models import Employee


def index(request):
    return render(request, 'index.html')


def build_employee_tree(employees):
    nodes = {}
    for employee in employees:
        nodes[employee.pk] = {'employee': employee, 'children': []}

    roots = []
    for employee in employees:
        if employee.manager_id is None:
            roots.append(nodes[employee.pk])
        else:
            parent = nodes.get(employee.manager_id)
            if parent is not None:
                parent['children'].append(nodes[employee.pk])

    return roots


def tree(request):
    employees = Employee.objects.select_related('manager').order_by('name')
    return render(request, 'tree.html', {'nodes': build_employee_tree(employees)})