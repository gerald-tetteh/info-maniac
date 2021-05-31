from info_maniac import app, db, bcrypt
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, current_user
from info_maniac.models import JobItem, User,WishlistItem
from info_maniac.scraper import search_jobberman_scraper
from info_maniac.forms import RegisterForm, LoginForm
import json

@app.route("/")
def home():
  job_items = JobItem.query.all()
  wishlist_items =[]
  try:
    wishlist_items = current_user.wishlist
  except  Exception as e:
    print(e)
  print(wishlist_items)
  source_urls = [item.source_url for item in wishlist_items]
  return render_template("home.html", header_text="info maniac", show_search=True, job_items=job_items, source_urls=source_urls ,path="/", value="")

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
    email = form.email.data
    password = form.password.data
    user = User.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.password,password):
      login_user(user)
      flash("Login successful","success")
      return redirect(url_for("home"))
    else:
      flash("Email or password is incorrect","danger")
      return render_template("login.html", header_text="Login", show_search=False, path="/login", form=form)
  return render_template("login.html", header_text="Login", show_search=False, path="/login", form=form)

@app.route("/logout")
def logout():
  logout_user()
  return redirect(url_for("home"))
    
@app.route("/search", methods=["POST"])
def search():
  input_query=""
  if request.method == "POST":
    input_query = request.form['search_query']

  print(input_query)
  job_items = JobItem.query.filter(JobItem.title.contains(input_query))
  print(job_items)
  return render_template("home.html", header_text="info maniac", show_search=True, job_items=job_items, path='/search', value=input_query) 


@app.route("/wishlist")
def wishlist():
  job_items = current_user.wishlist
  return render_template("wishlist.html", header_text="Hey Hilda", show_search=False, job_items=job_items,path="", value="")

  
@app.route("/add-to-wishlist", methods=["POST"])
def add_to_wishlist():
  if request.method == "POST":
    data = json.loads(request.data)
    wishitem = WishlistItem(
      title = data["title"],
      company = data["company"],
      source_url = data["source_url"],
      image_url = data["image_url"],
      source_name = data["source_name"],
      job_type = data["job_type"],
      user_id = data["userId"]
    )
    current_user.wishlist.append(wishitem)
    db.session.commit()

    return {
      "messages":"successful"
    }

@app.route("/remove-wishlist-item", methods=["POST"])
def remove_wishlist_item():
  id = int(json.loads(request.data)["id"])
  print(type(id))
  wishlist_items = current_user.wishlist
  item = list(filter(lambda x: x.id == id, wishlist_items))[0]
  print(item)
  db.session.delete(item)
  db.session.commit()
  return {}