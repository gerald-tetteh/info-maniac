from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import atexit
from apscheduler.schedulers.background import  BackgroundScheduler

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SECRET_KEY"] = "621ce3fc-6aa9-4978-a4ec-6709008323e2"

db = SQLAlchemy(app)

from info_maniac.models import *
from info_maniac.scraper import scrape_and_save
import info_maniac.routes

# starting scheduler 
# scheduler = BackgroundScheduler()
# scheduler.add_job(scrape_and_save,'interval', seconds=3600)
# scheduler.start()

# #shutting down server
# atexit.register(lambda: scheduler.shutdown())