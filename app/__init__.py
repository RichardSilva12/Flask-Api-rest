from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+os.path.join(basedir, "default.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Init DataBase
db = SQLAlchemy(app)
# Init Marshmallow
ma = Marshmallow(app)

from .models import database, marshmallow
from .controllers import routes
