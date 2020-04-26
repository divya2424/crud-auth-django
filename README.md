# crud-auth-django

Basic CRUD and authentication using django

Steps to start the project and create enviornment :-

1. virtualenv --python=python3 venv
2. source venv/bin/activate
3. pip install -r requirements.txt
   (if you install new packages then don;t forget to put in the requirement file
   a) pip freeze (to check ur installed depencies)
   b. pip freeze > requirement.txt (to put your dependencies in your file)
   )
4. python manage.py runserver (Run the server)

Steps for migration :-

1. python manage.py makemigrations
2. python manage.py migrate

To create superuser

1.  python manage.py createsuperuser
