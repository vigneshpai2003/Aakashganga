from flask import *
app=Flask(__name__)

# uploading other python files
import blog
import config

if __name__ == '__main__':
	
	app.run(host='0.0.0.0',debug=True)
  
