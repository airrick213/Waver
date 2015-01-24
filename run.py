from flask import Flask
import jinja2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
