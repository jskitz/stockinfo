#Simple Stock Info App

##Installation instructions (tested on Ubuntu)

These instructions assume that node.js and npm are already installed.

Install the database

    sudo apt-get install sqlite3 libsqlite3-dev

Setup virtualenvwrapper, django, and django rest framework

    pip install virtualenvwrapper
    pip install django djangorestframework markdown django-filter ipython
    pip install yahoo-finance

Pull the project down from github into a source directory


Add the settings path to the environment

    export DJANGO_SETTINGS_MODULE=stockinfo.settings