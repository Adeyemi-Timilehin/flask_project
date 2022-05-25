from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:abc@localhost:5432/example'
db = SQLAlchemy(app)

class Person(db.Model):
  __tablename__ = 'persons'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)




Foreign key is stored on the child table and not on the parent mapping a reltaionship between the parent to child, then use select join to have access to them
### Joining from child to parent
##### Parent model uses relationship and child models uses foreign keys



class Drive (db.model):
  __tablename__ = 'drivers'
  id = db.Column(db.Integer, primary_key=true)
  ...
  vehicles = db.relationship)'Vehicle',backref='drivers,lazy=true)


class Vehicle (db.model):
  __tablename__ = 'vehicles'
  id = db.Column(db.Integer, primary_key=true)
  make = db.Column(db.String(), nullable=False_
  ...
  driver_id = db.Column(db.Integer, db.ForeignKey('drivers.id'),nullable=False)
