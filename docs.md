# Setting up a virtual env

$ mkdir myproject
$ cd myproject
$ python3 -m venv web_server
$ . venv/bin/activate

## HTTP Server Setup

- https://docs.python.org/3/library/http.server.html: Not for production

# Flask

https://flask.palletsprojects.com/en/2.2.x/

## Server Setup

https://flask.palletsprojects.com/en/2.2.x/quickstart/

## Run app

flask --app server run

## Turn the debug mode on to refresh automatically

$ flask --app server --debug run

## CSV Module

https://docs.python.org/3/library/csv.html

## MIME Type - How data is served to the browser

https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types

## installs the required dependencies when pushing to production

pip3 freeze > requirements.txt
