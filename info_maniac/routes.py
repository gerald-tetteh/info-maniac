from info_maniac import app
from flask import render_template, redirect, url_for
from info_maniac.models import JobItem

@app.route("/")
def home():
  job_items = JobItem.query.all()
  return render_template("home.html", header_text="info maniac", show_search=True, job_items=job_items,path="/")

@app.route("/jobberman")
def jobberman():
  job_items = JobItem.query.filter_by(source_name="Jobberman").all()
  return render_template("home.html", header_text="info maniac", show_search=True, job_items=job_items,path="/jobberman")

@app.route("/times-jobs")
def times_jobs():
  job_items = JobItem.query.filter_by(source_name="TimesJobs").all()
  return render_template("home.html", header_text="info maniac", show_search=True, job_items=job_items,path="/times_jobs")   

@app.route("/search", methods=["POST"])
def search():
  return redirect(url_for("home"))

  

