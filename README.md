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

IMPORTANT: there are two ways to connect Python to MySQL (mysql-connector or mysql-connector-python). We must find out which one works in our setup and uninstall the other.

- Browser:

7. Download and install MySQL Community Version (https://dev.mysql.com/downloads).

## Create Project + App

- Git Bash:

8. django-admin startproject dcrm (do not accept special character)
9. cd dcrm (change directory)
10. python manage.py startapp website

Tips: `ls` lists files in the current directory and `clear` clears the window.

## Open Project + Settings

- VS Code:

Always activate the virtual environment on the cmd terminal when oppening the VS Code.
C:\Users\Xis\OneDrive\Documentos\VSCodeProjects\django-crm\venv\Scripts\activate
ctrl + shift + p -> Python: Select Interpreter -> Select Virtual Environment Interpreter

11. Open Project Folder
12. dcrm/settings.py: add website to the INSTALLED_APPS
13. dcrm/settings.py: change the default DATABASES ENGINE from sqlite3 to mysql
14. dcrm/settings.py: change the NAME of the DB and add MySQL USER/PASSWORD/HOST/PORT

## Create MySQL Connection and Database

- VS Code

15. DCRM: New File -> mydb.py
16. mydb.py: import mysql.connector, create a variable to make the connection, prepare a cursor and create the database.
17. mydb.py: Run Python File (create the DB at MySQL)
18. (venv) cmd terminal: python manage.py migrate (push standard Django tables to the DB)

## Create Super User and Run Server

18. (venv) cmd terminal: python manage.py createsuperuser (admin/admin123)
19. (venv) cmd terminal: python manage.py runserver (http://127.0.0.1:8000/)

## Version Control with Git

20. git config --global user.name "Thiago Tavares"
21. git config --global user.email "tfreitast88@gmail.com"
22. git config --global push.default matching
23. git config --global alias.co checkout
24. git init
25. git add .
26. git status
27. git commit -m "project, app and database"
28. git remote add origin https://github.com/thiago-freitas-tavares/django-crm.git`
29. git push -u origin main

## Build Basic App

30. website: New Folder -> templates
31. website/templates: New File -> index.html (template)
32. website/views.py: create fisrt view function called index (view)
33. website: New File -> urls.py
34. website/urls.py: import path and views to create a URL to the home page (URL)
35. dcrm/urls.py: import include and add website.urls.py path to the urlpatterns.
36. website/templates: New File -> base.html (base to every page of the website)
37. https://getbootstrap.com: Docs -> Quick Start 2 -> Copy to clipboard
    Bootstrap is a front-end framework in HTML, CSS and JavaScript.
38. website/templates/base.html: Paste code (every page of the website will refer to this doc)
39. website/templates/base.html: Change the `title` to Django CRM
40. website/templates/base.html: At `body` remove the `h1` tag and add a `block content` in order to pull content from the webpages.
41. website/templates/index.html: `extends base.html` and add a `block content` to be pulled
42. website/templates/base.html: `block content` inside a `div` container tag for formatting

## Create and Format Navbar

43. website/templates: New File -> navbar.html
44. https://getbootstrap.com: Docs -> Components (Navbar) -> Copy to clipboard (all sub-components)
45. website/templates/navbar.html: Paste code
46. website/templates/base.html: include navbar.html
47. website/templates/navbar.html: change `nav` tag `class` to dark mode (navbar-dark bg-dark)
48. website/templates/navbar.html: change `a` tag to Django CRM and `href` to the home page
49. website/templates/navbar.html: remove Home, Dropdown, Disabled and the Search tool.

## Users Log in and Log out

50. website/views.py: import Django authentication system and pop-up messages
