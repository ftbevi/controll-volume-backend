ARGS = $(filter-out $@,$(MAKECMDGOALS))

build:
	docker-compose build

clean:
	docker-compose kill && docker-compose down --rmi all
	sudo rm -rf data/
	sudo rm -rf statics/
	sudo rm -rf .pytest_cache/

createsuperuser:
	docker-compose run app poetry run python manage.py shell -c "from django.contrib.auth.models import User; \
	u, _ = User.objects.get_or_create(email='dev@controllstore.co'); \
	u.username = 'dev'; \
	u.set_password('controllstore@#2024'); \
	u.is_superuser = u.is_staff = True; \
	u.save(); \
	print('Superuser: dev / controllstore@#2024');"

statics:
	docker-compose run --rm app poetry run python manage.py collectstatic --noinput

migrate:
	docker-compose run --rm app poetry run python manage.py migrate

migrations:
	docker-compose run --rm app poetry run python manage.py makemigrations

dbupdate: migrations migrate

dbunaccent:
	docker-compose exec postgres psql -U controllvolumes -c "CREATE EXTENSION IF NOT EXISTS UNACCENT;"

precommit:
	pre-commit install
	pre-commit autoupdate

lint:
	docker-compose run --rm app poetry run autoflake -i -r --remove-all-unused-imports --remove-unused-variables --ignore-init-module-imports .
	docker-compose run --rm app poetry run isort -rc --atomic --multi-line=3 --trailing-comma --force-grid-wrap=0 --use-parentheses --line-width=88 .

services:
	docker-compose up -d postgres

setup: build services dbupdate dbunaccent createsuperuser statics

bash:
	docker-compose run --rm $(ARGS) sh

test:
	docker-compose run --rm app poetry run pytest -s

shell_plus:
	docker-compose run --rm app poetry run python manage.py shell_plus

stop:
	docker-compose down --remove-orphans

run:
	docker-compose run --rm --service-ports app poetry run python manage.py runserver 0.0.0.0:6600
