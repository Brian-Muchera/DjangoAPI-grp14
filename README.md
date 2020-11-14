# Hospital Management System

## Description
 This is a backend project for generating a Django API to be linked to a frontend project

 ## Prerequisites

   - Ubuntu Software
   - Python3.8
   - Postgress
   - python virtualenv

 ## Clone the Repo

Run the following command on the terminal: git clone https://github.com/Brian-Muchera/DjangoAPI-grp14.git
    &&
cd DjangoAPI-grp14

## Activate virtual environment

    Activate virtual environment using python3.8 as default handler

    virtualenv -p /usr/bin/python3.8 venv && source venv/bin/activate

 ## Install dependancies

Install dependancies that will create an environment for the app to run pip3 install -r requirements.txt
Create the Database

    psql
    CREATE DATABASE brian1;

 ## .env file

Create .env file and paste paste the following filling where appropriate:

    SECRET_KEY = '<Secret_key>'
    DBNAME = 'brian1'
    USER = '<Username>'
    PASSWORD = '<password>'
    DEBUG = True



 ## Run initial Migration

    python3.8 manage.py makemigrations app
    python3.8 manage.py migrate

 ## Run the app

    python3.8 manage.py runserver

    Open terminal on localhost:8000
 ## Known bugs

None for now!!

 ## Technologies used

- [Python3.8](https://www.python.org/)
- [Django 3.1.2](https://docs.djangoproject.com/en/2.2/)
- [Heroku](https://heroku.com)

**Contact us at**
- mucherabrian2@gmail.com 
- katmuema@gmail.com
- catherinekanini001@gmail.com
- okotojr@gmail.com
- mattasamuel3@gmail.com
- tonyishangu@gmail.com

if you run into any issue or have any questions

## License

- [![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](https://github.com/Brian-Muchera/DjangoAPI-grp14.git)