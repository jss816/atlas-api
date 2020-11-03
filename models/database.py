from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import abort

db = SQLAlchemy()
ma = Marshmallow()