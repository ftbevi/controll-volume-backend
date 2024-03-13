# Controll Volume

System for controll sediments.

## Build Instructions

1. create .env file using .env-example file.
```
ALLOWED_HOSTS=*
DEBUG=True
DATABASE_URL=postgres://[user_db]:[password_db]@db:5432/[database_name]
SECRET_KEY=secret_key
PROJECT_ENVIRONMENT=local

```

2. Run command for install e configure development environment.

```bash
make setup
```

3. Run command for execute project. open in you browser http://localhost:6600/ and go direct in admin.

```bash
make run
```

4. make login using credentials created in make setup command.

```
user: dev
password: controllstore@#2024
```

When your avaliation is finish, then run command for kill all container.

## Interesting Commands

When your avaliation is finish, then run command for kill all container.

```bash
make stop
```

Command for update database executing makemigrations and migrate.

```bash
make dbupdate
```

Command for execute just makemigrations.

```bash
make makemigrations
```

Command for execute just migrate.

```bash
make migrate
```

Command for clean dev environment fully.

```bash
make clean
```



### Third-party Libraries
- celery
- django rest framework
- pytest
- pytest-django
- faker
- factory boy
- ipdb
- django extensions
- ipython
- factory-boy
- pytest-factoryboy
- dj-database-url
- python-decouple
