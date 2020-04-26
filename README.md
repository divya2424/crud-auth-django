# crud-auth-django

Basic CRUD and authentication using django

Steps to start the project and create enviornment :-

1. virtualenv --python=python3 venv
2. source venv/bin/activate
3. pip install Django==2.0.3
4. pip install djangorestframework
5. pip freeze (to check ur installed depencies)
6. pip freeze > requirement.txt (to put your dependencies in your file)
7. python manage.py runserver (Run the server)

Steps for migration :-

1. python manage.py makemigrations
2. python manage.py migrate

To create superuser

1.  python manage.py createsuperuser
