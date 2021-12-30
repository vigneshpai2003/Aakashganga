from flask import *

app=Flask(__name__)

import blog


@app.route('/')
def index():
	return render_template("index.html")


if __name__ == '__main__':
	app.run(debug=True)
