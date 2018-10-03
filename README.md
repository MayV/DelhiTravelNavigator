# DelhiTravelNavigator
A web application which gives shortest route as well as multiple best routes for buses and metro in Delhi along with total price of travel. Also gives information about the buses and metro lines. A database is attached with the web application. So best routes and other information is calculated dynamically when user gives input. Uses Depth First Search (DFS) algorithm with Backtracking algorithm over data fetched from sqlite database.
# Frameworks/ Languages/ Database
Django web framework, Python, HTML, CSS and Sqlite database.

#### Installation
- Clone this repository: git clone git@github.com:MayV/DelhiTravelNavigator.git
- cd into  DelhiTravelNavigator.
- Install pyenv.
- Install pyenv-virtualenv.
- Install Python 3.5.2: pyenv install 3.5.2.
- Create a new virtualenv called productionready: pyenv virtualenv 3.5.2 productionready.
- Set the local virtualenv to productionready: pyenv local productionready.
- Reload the pyenv environment: pyenv rehash.
