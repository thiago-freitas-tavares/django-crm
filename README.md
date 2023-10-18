# Django CRM Project

## Create Virtual Environment + Installations

- Project Folder:

1. Right Click -> Git Bash Here

- Git Bash:

2. python -m venv venv
3. source venv/Scripts/activate
4. pip install django
5. pip install mysql
6. pip install mysql-connector-python

- IMPORTANT: there are two ways to connect Python to MySQL (mysql-connector or mysql-connector-python). We must find out which one works in our setup and uninstall the other.

- Browser:

7. Download and install MySQL Community Version (https://dev.mysql.com/downloads).

## Create Project + App

- Git Bash:

8. django-admin startproject dcrm (nao aceita caractere eespecial)
9. cd dcrm
10. python manage.py startapp website

## Open Project + Settings

- VS Code:

- Always activate the virtual environment on the cmd terminal when oppening the VS Code.
- C:\Users\Xis\OneDrive\Documentos\VSCodeProjects\django-crm\venv\Scripts\activate
- ctrl + shift + p -> Python: Select Interpreter -> Select Virtual Environment Interpreter

11. Open Project Folder
12. settings.py: add website to the INSTALLED_APPS
13. settings.py: change the default DATABASES ENGINE from sqlite3 to mysql
14. settings.py: change the NAME of the DB and add MySQL USER/PASSWORD/HOST/PORT

## Create MySQL Connection and Database

- VS Code

15. DCRM: New File -> mydb.py
16. mydb.py: import mysql.connector, create a variable to make the connection, prepare a cursor and create the database.
17. (venv) cmd terminal: python manage.py migrate

## Create Super User and Run Server

18. (venv) cmd terminal: python manage.py createsuperuser (admin/admin123)
19. (venv) cmd terminal: python manage.py runserver (http://127.0.0.1:8000/)

commands
ls -> lists the files in the current directory
clear - limpa tela
cd - move para o diretorio especifico
