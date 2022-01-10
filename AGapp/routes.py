from flask import render_template
from AGapp import app
from AGapp.models import User, Aakashvani, Post, Comment, Event


def sortByPriority(model):
	return sorted(model.query.all(), key=lambda x: x.priority)


@app.route('/')
def index():
	return render_template("index.html", events=sortByPriority(Event))

@app.route('/team')
def team():
	return render_template('team.html')

@app.route('/aakashvani')
def aakashvani():
	return render_template('aakashvani.html', aakashvani=sortByPriority(Aakashvani))

@app.route('/aakashvani/<aakashvani_id>/<post_priority>')
def aakashvani_post(aakashvani_id, post_priority):
	aakashvani = Aakashvani.query.filter_by(id=int(aakashvani_id)).first()
	posts = sorted(aakashvani.posts, key=lambda x: x.priority)
	current_post = posts[int(post_priority) - 1]

	return render_template('post.html',
	 						aakashvani=aakashvani,
							nposts=list(range(1, len(posts)+1)),
							current_post=current_post,
							current_post_no=int(post_priority))

@app.route('/events')
def events():
	return render_template('events.html')

@app.route('/gallery')
def gallery():
	return render_template('gallery.html')

@app.route('/facilities')
def facilities():
	return render_template('facilities.html')

@app.route('/dhruv')
def dhruv():
	return render_template('dhruv.html')
