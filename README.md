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
	./manage.py migrate          # Creates the database models
	./manage.py createsuperuser  # admin, admin@example.com, password
	./manage.py collectstatic    # moves assets to static directory
	./manage.py import_stocks    # imports the stocks to the database
	./manage.py runserver        # runs the django web server at port 8000

Navigate to http://localhost:8000/api/ and login using admin credentials from above.

* http://localhost:8000/api/stocks/?q=AAP - endpoint for doing a simple prefix match
* http://localhost:8000/api/stocks/history/?symbol=YHOO - for getting a month worth of historic data.  This endpoint would likely change based on IDs once I get Ember working.

###Frontend setup

*Work in progress*

This part of the project is not yet completed.  Roughly 8 hours was spent trying to ramp up on ember-cli, but haven't learned enough yet to be able to move forward.  Because Django templates also use the {{ }} syntax, each of the handlebar templates need to be wrapped in verbatim tags to stop django from processing them.  This is a rather large annoyance that makes me rethink using Django for the backend.  In any case, I started with what I knew in order to make progress.



