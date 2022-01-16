# KhoahocT3H
Khoahoc_Django_T3H

create SQL postgreSQL:

  - Install PostgreSQL

  - create database t3h_db; -->  sua file Setting.py

  - DATABASES = {
  
    'default': {
    
        'ENGINE': 'django.db.backends.postgresql',
        
        'NAME': 't3h_db',
        
       }
       
      }

Cai dat module psycopg2:

  pip install -U pip
  
  pip install psycopg2 or pip install psycopg2-binary
  
Sau khi cai xong Check: python manage.py check

Create superuser:

  - python manage.py migrate
  
  - python manage.py createsuperuser: admin/1
