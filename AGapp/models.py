from datetime import datetime
from flask_admin.contrib.sqla import ModelView
from AGapp import db, admin


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='user', lazy=True)

    def __repr__(self):
        return f"User({self.id}, {self.username})"


# class Aakashvani(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     posts = db.relationship('Post', backref='user', lazy=True)

#     def __repr__(self):
#         return f"User({self.id}, {self.title})"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    data = db.Column(db.Text, nullable=False)
    comments = db.relationship('Comment', backref='post', lazy=True)

    def __repr__(self):
        return f"Post({self.id}, {self.title}, {self.user_id})"


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    comment = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Comment({self.id}, {self.post_id}, {self.comment})"


admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Comment, db.session))