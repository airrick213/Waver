from flask import Flask, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

app.debug = True

app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
