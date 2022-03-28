Chef-Blog
===============

____

About
-----

___

**Chef blog with recipes**

**Author: Victor Kozlov**

**Email: *[victorkozlov1999@mail.ru](victorkozlov1999@mail.ru)***

**Requirements**:

    Python 3.9, PostgreSQL, Django 


## Setup development environment

##### 1) Clone repository

    git clone git@github.com:<your-username>/<your-repository>.git

##### 2) Создать виртуальное окружение

    virtualenv -p python3.9 --prompt=<name-your-virtual>- venv/
    
##### 3) Create a virtual environment
    
    source venv/bin/activate

##### 4) Install pip packages

    pip install -r requirements.txt

##### 5) Set up PostgreSQL

##### 6) Run migration

    python manage.py migrate
    
##### 7) Create superuser

    python manage.py createsuperuser
    
##### 8) Run server

    python manage.py runserver

