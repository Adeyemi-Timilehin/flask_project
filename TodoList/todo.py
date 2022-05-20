from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:tolu1992@localhost:5432/timik'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Todo(db.Model):
    __tablename__='todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(),nullable=False)
    completed = db.Column(db.Boolean, nullable=True, default=False)

    def __repr__(self):
        return f'<Person ID: {self.id}, name: {self.name}>'