from info_maniac import db
from datetime import datetime

class JobItem(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.Text, nullable=False)
  company = db.Column(db.Text, nullable=False)
  source_url = db.Column(db.Text, nullable=False)
  image_url = db.Column(db.Text, nullable=False, default="default.png")
  date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  source_name = db.Column(db.Text, nullable=False)
  job_type = db.Column(db.Text, nullable=False, default="Unknown")

  def __repr__(self) -> str:
    return f"JobItem({self.title},{self.company},{self.source_name})"