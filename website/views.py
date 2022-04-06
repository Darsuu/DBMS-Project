#stores all the routes the user can go to
from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")

@views.route('/link1')
def link1():
    return "<h1>Link1</h1>"

@views.route('/link2')
def link2():
    return "<h1>Link2</h1>"

@views.route('/link3')
def link3():
    return "<h1>Link3</h1>"