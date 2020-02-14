To install dependencies, run the following:

```
pip3 install flask Flask-Uploads
```

Due to current issues with Werkzeug, another 3rd party dependency, I also had to do the following:

```
pip3 uninstall werkzeug
pip3 install werkzeug==0.16.1
```

How to run the server in debug mode:

```
cd flask_server
export FLASK_APP=server.py
export FLASK_DEBUG=1
flask run
```
