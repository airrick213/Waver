from config import app, render_template
import jinja2
import os

@app.route('/')
def index():
    return render_template('index.jade')

@app.route('/login')
def login():
    return render_template('login.jade')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port,debug=True)
