1. First we have to install the python .basically in linux already python are installed at the time of installing the linux into the machine.
2.then we have to install the django framework in that various activities we have to do like install the virtual enviornement , create project and all after installing the project we have create the superuse for showing the backend activities in the project.

command to setup the django 

sudo apt install python3
sudo apt install python3-pip
pip3 install virtualenv
python3 -m virtualenv Env
which python3

source Env/bin/activate
pip3 install django
pip list
cd Env/
django-admin startproject myapp
python manage.py runserver


3.then we have to choose the database which we want.basically django provide its own database name is sqlite3 . but according to the requirements of client and all we have to setup different databases.and whenever you use the different database then you have to add the below code in the settings.py file it is mandatory to add the code in that file so then and then we are connet to the database 


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'your database name',
        'USER':'user name',
        "PASSWORD":'your password',
        "HOST":'localhost',
        "PORT":'5432',
    }
}


--------------------------------------------------------------------------
1.to start the postgres terminal use below command

sudo su - postgres
--------------------------------------------------------------------------
2.then you have use below command to open the shell

psql
--------------------------------------------------------------------------
3.then create the database by using the below command

CREATE DATABASE my_db;
--------------------------------------------------------------------------
4.to show the database by using below command

\l
--------------------------------------------------------------------------
5.after that you have to create the user and password 

create user myuser with encrypted password 'mypass';
-----------------------------------------------------------------------
6.add the privileges to the user

grant all privileges on database mydb to myuser;
-------------------------------------------------------------------------
7.if given error occur the use below command

ERROR 

psycopg2.errors.InsufficientPrivilege: permission denied for relation django_migrations

then use below command

python -m pip install psycopg2

then 

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public to admin;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public to admin;
GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public to admin;

----------------------------------------------------------------------------
8.if we have to see the table in the database so first we have to select that database by using the below command    /connect the database first 

use this command to connect the database

\c db_movie

then use \dt to see the content of the database


4.whenever if you create the database then you have to must do the migrations.the migrations many those changes you have done that you have to reflect on the user interface then and then you do the migrations.

first you have to use makemigrations command like  this

python manage.py makemigrations  

after that you have to use the below command

python manage.py makemigrations  

after using this command the database schema is createed.

