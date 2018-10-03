# DelhiTravelNavigator
A web application which gives shortest route as well as multiple best routes for buses and metro in Delhi along with total price of travel. Also gives information about the buses and metro lines. A database is attached with the web application. So best routes and other information is calculated dynamically when user gives input. Uses Depth First Search (DFS) algorithm with Backtracking algorithm over data fetched from sqlite database.

# Frameworks/ Languages/ Database
Django web framework, Python, HTML, CSS and Sqlite database.
# Cloning Install Virtualenv getting started:

```bash
$ pip install virtualenv
$ virtualenv my_project
$ cd my_project_folder
```

To clone, you just need to access your git/terminal and use the command below:

```bash
$ git clone https://github.com/MayV/DelhiTravelNavigator.git
$ cd DelhiTravelNavigator

```

After that, you must:
* Install the dependencies (Django framework)
* Have access to Sqlite databse
* After installing, you need to run the migration command inside the project directory (`python manage.py migrate`)
* And finally, start the server (`python manage.py runserver`)

# Running in Virtual Environment
If pip is not installed:
Download: [pip](https://bootstrap.pypa.io/get-pip.py)
Execute this command in the same folder in which you have downloaded get-pip.py:
```
$ python get-pip.py
```
Now use pip to install virtualenv
```
$ pip install --user pipenv
```

To create a virtualenv, run:
```
  $ virtualenv folder_name
```

To start using that virtualenv, run:
```
$ source folder_name/bin/activate
```
You can use ```$ deactivate``` to if close this virtualenv.
