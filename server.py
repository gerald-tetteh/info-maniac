from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from apscheduler.schedulers.background import  BackgroundScheduler
from scraper import scrape_from_jobberman

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

db = SQLAlchemy(app)

@app.route("/")
def home():
  return render_template("layout.html")



# starting scheduler 
scheduler = BackgroundScheduler()
scheduler.add_job(func=scrape_from_jobberman(), trigger='interval', seconds=60)
scheduler.start()



if __name__ == "__main__":
  app.run(debug=True,host="0.0.0.0")