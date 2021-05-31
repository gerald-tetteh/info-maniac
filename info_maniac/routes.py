from info_maniac import app
from flask import render_template, redirect, url_for, request
from info_maniac.models import JobItem
from info_maniac.scraper import search_jobberman_scraper

@app.route("/")
def home():
  job_items = JobItem.query.all()
  return render_template("home.html", header_text="info maniac", show_search=True, job_items=job_items,path="/", value="")

@app.route("/jobberman")
def jobberman():
  job_items = JobItem.query.filter_by(source_name="Jobberman").all()
  return render_template("home.html", header_text="info maniac", show_search=True, job_items=job_items,path="/jobberman", value="")

@app.route("/times-jobs")
def times_jobs():
  job_items = JobItem.query.filter_by(source_name="TimesJobs").all()
  return render_template("home.html", header_text="info maniac", show_search=True, job_items=job_items,path="/times_jobs", value="")   

@app.route("/search", methods=["POST"])
def search():
  input_query=""
  if request.method == "POST":
    input_query = request.form['search_query']

  print(input_query)
  job_items = JobItem.query.filter(JobItem.title.contains(input_query))
  print(job_items)
  return render_template("home.html", header_text="info maniac", show_search=True, job_items=job_items, path='/search', value=input_query) 

  

