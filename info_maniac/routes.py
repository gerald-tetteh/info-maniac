from info_maniac import app, db, bcrypt
from flask import render_template, redirect, url_for, request
from info_maniac.models import JobItem, User
from info_maniac.scraper import search_jobberman_scraper
from info_maniac.forms import RegisterForm, LoginForm 

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

@app.route("/register", methods=["GET","POST"])
def register():
  form = RegisterForm()
  if form.validate_on_submit():
    first_name = form.first_name.data
    last_name = form.last_name.data
    email = form.email.data
    password = form.password.data
    hash_password = bcrypt.generate_password_hash(password)
    user = User(first_name=first_name, last_name=last_name, email=email, password=hash_password)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for("home"))
  return render_template("register.html", header_text="Register", show_search=False, path="/register", form=form) 

@app.route("/login", methods=["POST", "GET"])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    return redirect(url_for("home"))
  return render_template("login.html", header_text="Login", show_search=False, path="/login", form=form)
    

@app.route("/search", methods=["POST"])
def search():
  input_query=""
  if request.method == "POST":
    input_query = request.form['search_query']

  print(input_query)
  job_items = JobItem.query.filter(JobItem.title.contains(input_query))
  print(job_items)
  return render_template("home.html", header_text="info maniac", show_search=True, job_items=job_items, path='/search', value=input_query) 

  

