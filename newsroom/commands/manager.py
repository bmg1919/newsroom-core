# from flask_script import Manager
from newsroom.web.factory import get_app
from flask import Flask

app = get_app()
# manager = Manager(app)
flask = Flask(app)
