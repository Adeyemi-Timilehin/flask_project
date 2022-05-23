
from crypt import methods
from flask import Flask, render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import true

app = Flask(__name__)
db=SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:tolu1992@localhost:5432/todoApp'
class Todo(db.Model):
    __tablename__='todos'
    id=db.Column(db.Integer,primary_key=True)
    description=db.Column(db.String(),nullable=False)

def __repr__(self):
    return f'<Todo {self.id} {self.description}>'
db.create_all()


@app.route('/todos/create', methods=['POST'])
def create_todo():
  description = request.form.get('description')
  todo = Todo(description=description)
  db.session.add(todo)
  db.session.commit()
  return redirect(url_for('index'))


@app.route('/')
def index():
  return render_template('index.html', data=Todo.query.all())


#always include this at the bottom of your code (port 3000 is only necessary in workspaces)

if __name__ == '__main__':
  app.debug = true 
  app.run(host="0.0.0.0", port=3000)