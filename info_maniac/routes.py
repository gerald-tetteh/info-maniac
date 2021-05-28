from info_maniac import app
from flask import render_template, redirect, url_for
from info_maniac.models import JobItem

@app.route("/")
def home():
  job_items = JobItem.query.all()
  return render_template("home.html", header_text="info maniac", show_search=True, job_items=job_items)

@app.route("/search", methods=["POST"])
def search():
  return redirect(url_for("home"))