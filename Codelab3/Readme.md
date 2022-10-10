To build the database admin image from Docker local.
docker build -t mydba .

To run the database admin container 
docker run --name mydba --network mynetwork -p 8080:81 -d mydba

To build the database image from Docker local
docker build -t mydb .

To run the database container from the local
docker run --name mydb --network mynetwork -itd -p5432:5432 mydb

To build the django app image from docker local
docker build -t mydjango . 

To run the django app conaitner
docker run -it -p8000:8000 -v "$(pwd)/app:/app" mydjango /bin/bash

django-admin startproject app

Change the database entries in the settings.py file :
'USER' = 'root', 'PASSWORD' = pass, 'HOST' = mydb, 'NAME' = web, 'PORT' = 5432

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'web',
        'USER': 'root',
        'PASSWORD': 'pass',
        'HOST': 'mydb',
        'PORT': 5432,
    }
}


Migrate
root@fcbb5da5d62a:/app# python /app/app/manage.py migrate

Create superuser
root@fcbb5da5d62a:/app# python /app/app/manage.py createsuperuser 
Username (leave blank to use 'root'): Email address: a@a.com 
Password: pass Password (again): pass

Run server
root@fcbb5da5d62a:/app# python /app/app/manage.py runserver 0.0.0.0:8000

Open the browser and type http://localhost:8081/browser/ and enter name: mydb, root, pass

Open http://localhost:8000/admin/ and enter  user : root , password : pass


