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
`ctrl + shift + p` -> Python: Select Interpreter -> Select Virtual Environment Interpreter

11. Open Project Folder (second folder without the venv)
12. dcrm/settings.py: add `website` to the `INSTALLED_APPS`.
13. dcrm/settings.py: change the default `DATABASES ENGINE` from sqlite3 to mysql.
14. dcrm/settings.py: change the `NAME` of the DB and add MySQL `USER`/`PASSWORD`/`HOST`/`PORT`.

## Create MySQL Connection and Database

- VS Code:

15. DCRM: New File -> mydb.py
16. mydb.py: import `mysql.connector`, create a variable to make the connection, prepare a `cursor` and create the database.
17. mydb.py: Run Python File (creates the DB at MySQL)
18. (venv) cmd terminal: python manage.py migrate (push standard Django tables to the DB)

## Create Super User and Run Server

19. (venv) cmd terminal: python manage.py createsuperuser (admin/admin123)
20. (venv) cmd terminal: python manage.py runserver (http://127.0.0.1:8000/)

## Version Control with Git

- Git Bash (second folder without the venv):

21. git config --global user.name "Thiago Tavares"
22. git config --global user.email "tfreitast88@gmail.com"
23. git config --global push.default matching
24. git config --global alias.co checkout
25. git init
26. git add .
27. git status
28. git commit -m "project, app and database"
29. git remote add origin https://github.com/thiago-freitas-tavares/django-crm.git`
30. git push -u origin main

## Build Basic App

- VS Code:

31. website: New Folder -> templates
32. website/templates: New File -> index.html (template)
33. website/views.py: create fisrt `view function` called `index` (view).
34. website: New File -> urls.py
35. website/urls.py: import `path` and `views` to create a URL to the home page (URL).
36. dcrm/urls.py: import `include` and add `website.urls` path to the `urlpatterns`.
37. website/templates: New File -> base.html (base to every page of the website)
38. https://getbootstrap.com: Docs -> Quick Start 2 -> Copy to clipboard
    Bootstrap is a front-end framework in HTML, CSS and JavaScript.
39. website/templates/base.html: Paste code (every page of the website will refer to this doc).
40. website/templates/base.html: Change the `title` to Django CRM.
41. website/templates/base.html: At `body` remove the `h1` tag and add a `block content` in order to pull content from the webpages documents.
42. website/templates/index.html: `extends base.html` and add a `block content` to be pulled.
43. website/templates/base.html: `block content` inside a `div` tag container for formatting.

## Create and Format Navbar

44. website/templates: New File -> navbar.html
45. https://getbootstrap.com: Docs -> Components (Navbar) -> Copy to clipboard (all sub-components)
46. website/templates/navbar.html: Paste code.
47. website/templates/base.html: include `navbar.html`.
48. website/templates/navbar.html: change `nav` tag `class` to dark mode (navbar-dark bg-dark).
49. website/templates/navbar.html: change `a` tag to Django CRM and `href` to the home page.
50. website/templates/navbar.html: remove Home, Dropdown, Disabled and the Search tool (won't need).

## Users Log in

51. website/templates/index.html: we want the login page to be the home page, case the user is not logged in, so we create a login form with HTTP `POST` method inside the block content, pointing to the home page.
52. https://getbootstrap.com: Docs -> Forms (Overview) -> Copy to clipboard
53. website/templates/index.html: Paste code after the `csrf_token` (cross-site request forgery token to avoid malicious attacks).
54. website/templates/index.html: remove email `label`, change `input` `type` to text, include `name`/`placeholder`/`required` and remove `id`/`aria`.
55. website/templates/index.html: remove password `label`, include `input` `name`/`placeholder`/`required` and remove `id`.
56. website/templates/index.html: remove the `checkbox`.
57. website/templates/index.html: change button class `btn-primary` (blue) to `btn-secondary` (gray) and name to Login.
58. website/templates/index.html: create an `if` block so the login page is the home page, case the user is not logged in.
59. website/views.py: import Django authentication system and pop-up messages.
60. website/views.py: since the loggin page may also be the home page, we check if the HTTP request method is `POST` (sending data) or `GET` (requesting data) inside the `index` view function.
61. website/views.py: if `POST`, save username/password input in the username/password variables.
62. website/views.py: authenticate with Django's function and check if user variable is not `NULL`.
63. website/views.py: `if` user is not None, log the user in, showing a success message, and `redirect` (import function) to the home page.
64. website/views.py: `else` (if user is None), show an error message and `redirect` to the home page (login page).
65. website/views.py: `else` (if HTTP request method is not `POST`), render the `index.html` page.
66. website/templates/base.html: create an `if` and `for` block to display the messages from the `index` view function.
67. https://getbootstrap.com: Docs -> Components (Alerts) -> Copy to clipboard (Dismissing)
68. website/templates/base.html: Paste code inside the `for` block and change the bootstrap standard message.

## Users Log out

69. website/views.py: create `logout_user` view function.
70. website/urls.py: create an URL to the `logout_user` view function.
71. website/views.py: use Django's logout function to log the user out, showing a success message, and `redirect` to the home page.
72. website/templates/navbar.html: change bootstrap Link `nav-item` `a` tag to Logout and `href` to the logout page.
73. website/templates/navbar.html: `if` user is logged in, the `nav-item` should be Logout, `else`, it should be Login.

## Register Users

We can add users manually through the admin section, but we also want people to register on their own in the webpage.

74. website/views.py: create `register_user` view function.
75. website/urls.py: create an URL to the `register_user` view function.
76. website/templates: New File -> register.html
77. website/views.py: `return` render register.html at `register_user` view function.
78. website/templates/register.html: `extends base.html` and add a `block content` to be pulled.
79. website/templates/navbar.html: include a Register `nav-item` to the register page, case the user is logged out.
80. website: New File -> forms.py
81. website/forms.py: import `User`/`UserCreationForm` classes from Django's framework and create a `SignUpForm` class inheriting from `UserCreationForm`.
82. website/forms.py: import Django's `forms` module and set `email`, `first_name` and `last_name` variables.
83. website/forms.py: variables with empty `labels` (placeholder text instead), `widget` of text input fields with `attributes` to style the form. We'll be using bootstrap to style and it requires a class of `form-control`.
84. website/forms.py: create a class `Meta` to set the form's model and fields.
85. website/forms.py: create a constructor in the `SignUpForm` class to initialize the variables `username`, `password1` and `password2`.
86. website/views.py: import the `SignUpForm` class and check if the HTTP request method is `POST` or `GET` inside the `register_user` view function.
87. website/views.py: if `POST` (user clicking the Submit button), create a `SignUpForm` object with data from the request.
88. website/views.py: if the form is `valid`, save it and `authenticate`/`login` the user, showing a success message, and redirect to the home page.
89. website/views.py: `else` (if HTTP request method is not `POST` - user accessing the register page), create a `SignUpForm` object and render the `register.html` page, filling the context dictionary with the form (it passes the form to the register page so we can do something with it there).
90. website/views.py: repeat the `return` render outside the `if`/`else` statement, so the page is reaload in case of errors.
91. website/templates/register.html: create a form with HTTP `POST` method inside the block content, pointing to the same view (empty `action`).
92. website/templates/register.html: render the form as paragraph (`form.as_p`) after csrf_token and include a Submit button.
93. https://getbootstrap.com: Docs -> Components (Alerts) -> Copy to clipboard (Dismissing)
94. website/templates/register.html: Paste code inside the `if form.errors` block and change the bootstrap standard message, including the specific errors with a `for field`/`if field.errors` block.

## Database Model

95. website/models.py: create a class `Record` inheriting `models.Model` to create a table, defining its fields.
96. website/models.py: create a function `__str__`, which tells Django what to show when it needs to print out an instance of the model.
97. (venv) cmd terminal: python manage.py makemigrations (this command creates a `0001_initial.py` document inside `website/migrations` folder).
98. (venv) cmd terminal: python manage.py migrate (push the `website_record` table to the dcrm_db DB).
99. website/admin.py: import `Record` class from `models.py` and `register` it to the admin site, so we can access the table from there.
100. http://127.0.0.1:8000/admin/website/record/: add two records manually.

## View Records on Website

101. website/views.py: import `Record` class from `models.py` and create a `records` variable to grab everything that is currently on the table.
102. website/views.py: pass the `records` variable as the context dictionary in the `render` function that is after user's authentication, so we can do something with it at `index.html`.
103. website/templates/index.html: inside the `if user.is_authenticated` block, create and `if records` and `for record` blocks to show each of records in the home page.
104. website/templates/index.html: printing `{{ record }}` shows only the `first_name` and `last_name`, as defined at `models.py` `__str__` function, so we print each item separately.

## Bootstrap Table