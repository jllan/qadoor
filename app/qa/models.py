from ..dbs import db
from sqlalchemy import Column
from ..func import get_current_time

class Question(db.Model):

    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    content = db.Column(db.Text(1024), nullable=False)
    answers_count = db.Column(db.Integer, default=0)
    create_time = db.Column(db.DateTime, default=get_current_time)

    author_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
    author = db.relationship('User', backref=db.backref('questions', lazy='dynamic'), uselist=False)


class Answer(db.Model):

    __tablename__ = 'answers'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text(1024))
    comments_count = db.Column(db.Integer, default=0)
    create_time = db.Column(db.DateTime, default=get_current_time)

    author_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
    author = db.relationship('User', backref=db.backref('answers', lazy='dynamic'), uselist=False)

    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    question = db.relationship('Question', backref=db.backref('answers', lazy='dynamic'), uselist=False)


class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text(1024))
    create_time = db.Column(db.DateTime, default=get_current_time)

    author_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
    author = db.relationship('User', uselist=False)

    answer_id = db.Column(db.Integer, db.ForeignKey('answers.id'))
    answer = db.relationship('Answer', backref=db.backref('comments', lazy='dynamic'), uselist=False)
