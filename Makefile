install:
	uv sync --dev

dev-start:
	uv run python manage.py runserver

migrate:
	uv run python manage.py migrate