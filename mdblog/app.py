from flask import Flask
from flask import render_template
from .database import articles
from flask import request
from flask import redirect
from flask import url_for
from flask import session



flask_app = Flask(__name__)
flask_app.secret_key = b"\xfc}\x1f\x1b\x10\xb0\x86m\xe9\xdbvi\xc1\xfb\xe4\x8b9'xTkM?\x9d"

@flask_app.route("/")
def view_welcome_page():
    return render_template("welcome_page.html", text="Toto je text")

@flask_app.route("/about/")
def view_about():
    return render_template("about.html", text="Toto je text")

@flask_app.route("/admin/")
def view_admin():
    if "logged" not in session:
        return redirect(url_for("view_login"))
    return render_template("admin.html", text="Toto je text")

@flask_app.route("/articles/")
def view_articles():
    return render_template("articles.html", articles=articles.items())

@flask_app.route("/articles/<int:art_id>")
def view_article(art_id):
    article = articles.get(art_id)
    if article:
        return render_template("article.html", article=article)
    return render_template("article_not_found.html", art_id=art_id)

@flask_app.route("/login/", methods=["GET"])
def view_login():
    return render_template("login.html")

@flask_app.route("/login/", methods=["POST"])
def login_user():
    username = request.form["username"]
    password = request.form["password"]
    if username == "admin" and password == "admin":
        session["logged"] = True
        return redirect(url_for("view_admin"))
    else:
        return redirect(url_for("view_login"))

@flask_app.route("/logout/", methods=["POST"])
def logout_user():
    session.pop("logged")
    return redirect(url_for("view_welcome_page"))
