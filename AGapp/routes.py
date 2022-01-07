from flask import render_template
from AGapp import app


@app.route('/')
def index():
	return render_template("index.html")

@app.route('/team')
def team():
	return render_template('team.html')

@app.route('/aakashvani')
def aakashvani():
	return render_template('aakashvani.html')

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
