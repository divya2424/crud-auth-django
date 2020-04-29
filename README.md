# crud-auth-django

Basic CRUD and authentication using external API in DJANGO. Integrated Celery which is used to perform an asynchronous task queue based on distributed message passing. Task queues are used as a strategy to distribute the workload between threads/machines.To work with Celery, we also need to install RabbitMQ because Celery requires an external solution to send and receive messages. Those solutions are called message brokers

# Steps to start the project and create enviornment :-

1. virtualenv --python=python3 venv
2. source venv/bin/activate
3. pip install -r requirements.txt
   (if you install new packages then don;t forget to put in the requirement file
   a) pip freeze (to check ur installed depencies)
   b. pip freeze > requirement.txt (to put your dependencies in your file)
   )
4. python manage.py runserver (Run the server)

# Steps for migration :-

1. python manage.py makemigrations
2. python manage.py migrate

To create superuser

1.  python manage.py createsuperuser

# Steps to start and install a RabbitMQServer"
# Install
1. From the main documentation

# start/stop the server
1. Start -sudo service rabbitmq-server start 
2. Stop - sudo service rabbitmq-server stop
3. Restart - sudo service rabbitmq-server restart
4. Status - sudo service rabbitmq-server status

# Steps to start celery and check :

1. celery -A api worker -l beat -l info
2. celery worker -A api --loglevel=info
3. celery -A api flower
4. celery -A api beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
#   (After installing celery-beat remeber to run python manage.py migrate to get the tables in sync with your db)


