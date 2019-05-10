# Smitty Werbenjagermanjensen's Homework 4

Creation of a web app that automates rubrics' management to evaluate students in an academic context.
(Original description and interface by
[Lambda-Ideas](https://github.com/DCC-CC4401/2019-1-Lambda-Ideas)).

This repository includes the new and improved SWJJ Solutions' version, and implementations
for the fourth homework in Software Engineering course.


## Getting Started

This project is made in Python (3.7) using the IDE PyCharm.
Even though this IDE was used, it should be possible to be executed successfully from the terminal
regardless of the OS.


### Prerequisites

#### Pipenv
A tool that mixes Python's pip, Pipfiles and virtualenv to simplify and automatize the
installation of the packages needed to run the algorithm. To install use the following:

``` pip install pipenv ```


### Installing

The project uses the framework Django. To avoid version dificulties and simplifying installation
for new users it's heavily recommended to use Pipenv with the following command inside this project's directory:

``` pipenv install ```


## Executing

First it's necessary to start Pipenv console to install this project's framework.

``` pipenv shell ```

Next, run the following commands to configure Django:

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

(You can exit Pipenv's shell using `exit` or by pressing Ctrl + D. Also, remember to replace `python`
with whichever command matching the version you're using). 

From now on, you just need the following command to start this project's local server:

``` pipenv run python manage.py runserver```


## Developed With
* [Django](https://www.djangoproject.com/) - Python's web framework.
* [Pipenv](https://pipenv.readthedocs.io/en/latest/) - Python's packaging tool.
* [W3.CSS](https://www.w3schools.com/w3css/) - CSS framework.


## Authors

* **Brandon Peña** - [brandonHaipas](https://github.com/brandonHaipas)
* **Cristián Llull Torres** - [CILT](https://github.com/CILT)
* **David de la Puente** - [daviddelapuente](https://github.com/daviddelapuente)
* **Pablo Torres** - [pabtorres](https://github.com/pabtorres)
* **Sofía Castro** - [cinnamontea](https://github.com/cinnamontea)


##problemas
1) login:
 
 1.1)al hacer login, no se hace un checkeo de los inputs para posibles
 inyeciones sql o html (se debe revisar en Usuarios/views.py la funcion login)
 
 1.2)al registrarse, un usuario puede escribir un nombre ya existente (se debe mejorar
 registrar, se debe revisar en Usuario/views registro y quizas el modelo)
 
 1.3) si un usuario se logea y se equivoca, sale un error bastante feo (se debe revisar login)