from info_maniac import app
from flask import render_template, redirect, url_for

@app.route("/")
def home():
  return render_template("layout.html", header_text="info maniac", show_search=True)

@app.route("/search", methods=["POST"])
def search():
  return redirect(url_for("home"))