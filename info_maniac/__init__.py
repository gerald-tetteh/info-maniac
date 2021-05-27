from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from apscheduler.schedulers.background import  BackgroundScheduler


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

db = SQLAlchemy(app)

@app.route("/")
def home():
  return render_template("layout.html")



def tester():
  print("----------- Testing ------------")



# starting scheduler 
from info_maniac.scraper import scrape_from_jobberman
scheduler = BackgroundScheduler()
scheduler.add_job(tester,'interval', seconds=10)
scheduler.start()





if __name__ == "__main__":
  app.run(debug=True,host="0.0.0.0")
