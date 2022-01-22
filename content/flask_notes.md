Title: Flask notes
Date: 2022-01-15 22:23
Modified: 2022-01-15 22:23
Category: development
Tags: Flask, web, python 
Slug: flask-notes
Authors: mb256
Summary: Personal notes how to start with python web framework Flask.   

Setup Python virtual environment. Inside virtenv install flask framework (+ all dependencies).   

```
$ python -m pip install flask
```

Example of hello-world app:   

```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to my Flask application!"
```

Set environment variables:   

```
export FLASK_APP=flashcards.py
export FLASK_ENV=development
 
```

Start Python Flask server in development mode:   
```
python -m flask run
```

Web page is than visible locally and you can check it in your web-browser at:
```
127.0.0.1:5000
```
or
```
localhost:5000
```

