from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:abc@localhost:5432/example'
db = SQLAlchemy(app)

class Person(db.Model):
  __tablename__ = 'persons'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)


from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:abc@localhost:5432/todoapp'
db = SQLAlchemy(app)

class Todo(db.Model):
  __tablename__ = 'todos'
  id = db.Column(db.Integer, primary_key=True)
  description = db.Column(db.String(), nullable=False)

  def __repr__(self):
    return f'<Todo {self.id} {self.description}>'

db.create_all()

@app.route('/')
def index():
  return render_template('index.html', data=Todo.query.all())


#always include this at the bottom of your code
if __name__ == '__main__':
   app.run(host="0.0.0.0", port=3000)




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
