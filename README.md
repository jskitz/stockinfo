#Simple Stock Info App

##Installation instructions (tested on Ubuntu virtual machine)

###Backend server setup

These instructions assume that node.js and npm are already installed.

Install the database engine

    sudo apt-get install sqlite3 libsqlite3-dev

Setup virtualenvwrapper, django, django rest framework, and yahoo finance

    pip install virtualenvwrapper
    pip install django djangorestframework markdown django-filter ipython
    pip install yahoo-finance

Pull the project down from github into a source directory

	git clone https://github.com/jskitz/stockinfo.git
	export DJANGO_SETTINGS_MODULE=stockinfo.settings
	cd stockinfo
	./manage.py migrate  # Creates the database models
	./manage.py createsuperuser  # admin, admin@example.com, password
	./manage.py 

    