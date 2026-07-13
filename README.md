# Вебсайт с древовидной иерархией сотрудников

![Django Tests](https://github.com/your-username/abz-agency-python-test/actions/workflows/django-tests.yml/badge.svg)

ТЗ: [testovoe-zadanie-na-pozitsiyu-junior-python-developer.pdf](https://github.com/user-attachments/files/29798369/testovoe-zadanie-na-pozitsiyu-junior-python-developer.pdf)

## Описание

Проект представляет собой Django-приложение для отображения структуры сотрудников в виде дерева. В интерфейсе можно просматривать сотрудников, их должности, дату приема на работу и зарплату.

## Требования

- Python 3.12+
- uv

## Установка

```bash
make install
```

## Локальный запуск

```bash
make dev-start
```

Открыть приложение: http://127.0.0.1:8000/

## База данных и демо-данные

Применить миграции:

```bash
uv run python manage.py migrate
```

Заполнить базу тестовыми сотрудниками:

```bash
uv run python manage.py seed_employees --count 20
```

## Тесты

```bash
uv run python manage.py test
```

## CI/CD

Проект настроен на автоматический запуск тестов через GitHub Actions при пуше и создании pull request.
