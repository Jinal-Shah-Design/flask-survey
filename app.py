from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension 

app = Flask(__name__)
debug = DebugToolbarExtension)app

app.config['SECRET_KEY'] = "oh-so-secret"