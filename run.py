from flask import Flask, render_template
import os
import jinja2

app = Flask(__name__)

app.config['DEBUG'] = True

app.debug = True

app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

@app.route('/')
def index():
	return render_template('index.jade')

@app.route('/login')
def login():
	return render_template('login.jade')

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 8000))
	app.run(host='0.0.0.0', port=port, debug=True)