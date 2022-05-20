
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db=SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:tolu1992@localhost:5432/todoapp'
class Todo(db.Model):
    __tablename__='todos'
    id=db.Column(db.Integer,primary_key=True)
description=db.Column(db.string(),nullable=False)

def __repr__(self):
    return f'<Todo {self.id} {self.description}>'
db.create_all()
@app.route('/')
def index():
  return render_template('index.html', data=Todo.query.all())


#always include this at the bottom of your code (port 3000 is only necessary in workspaces)

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=3000)