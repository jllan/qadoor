# encoding: utf-8

from .qa import qa
from .flask_app import app
from .dbs import db
from .user import user


app.register_blueprint(qa)
app.register_blueprint(user)
