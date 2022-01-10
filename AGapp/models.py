from datetime import datetime
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate

from AGapp import app, db


admin = Admin(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='user', lazy=True)

    def __repr__(self):
        return f"User({self.id}, {self.username})"


class Aakashvani(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    posts = db.relationship('Post', backref='aakashvani', lazy=True)
    priority = db.Column(db.Integer, default=1)

    def __repr__(self):
        return f"Aakashvani({self.id}, {self.title})"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    aakashvani_id = db.Column(db.Integer, db.ForeignKey('aakashvani.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    data = db.Column(db.Text, nullable=False)
    comments = db.relationship('Comment', backref='post', lazy=True)
    priority = db.Column(db.Integer, default=1)

    def __repr__(self):
        return f"Post({self.id}, {self.title}, {self.user_id})"


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    comment = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Comment({self.id}, {self.post_id}, {self.comment})"


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_link = db.Column(db.String(300), nullable=False)
    is_video = db.Column(db.Boolean, default=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    priority = db.Column(db.Integer, default=1)


admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Aakashvani, db.session))
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Comment, db.session))
admin.add_view(ModelView(Event, db.session))
