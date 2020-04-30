from flask import Flask
from flask import render_template



flask_app = Flask(__name__)

@flask_app.route("/")
def view_welcome_page():
    return render_template("welcome_page.html", text="Toto je text")

@flask_app.route("/about/")
def view_about():
    return render_template("about.html", text="Toto je text")
