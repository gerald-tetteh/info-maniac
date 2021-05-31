from info_maniac import db
from datetime import datetime
from flask_login import UserMixin
from info_maniac import login_manager, db

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)

class JobItem(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.Text, nullable=False)
  company = db.Column(db.Text, nullable=False)
  source_url = db.Column(db.Text, nullable=False, unique=True)
  image_url = db.Column(db.Text, nullable=False, default="default.png")
  date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  source_name = db.Column(db.Text, nullable=False)
  job_type = db.Column(db.Text, nullable=False, default="Unknown")

  def __repr__(self) -> str:
    return f"JobItem({self.title},{self.company},{self.source_name})"

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.Text, nullable=False)
  last_name = db.Column(db.Text, nullable=False)
  email = db.Column(db.Text, nullable=False)
  password = db.Column(db.Text, nullable=False)
  date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  wishlist = db.relationship("WishlistItem", backref="user", lazy=True)
  
  def __repr__(self) -> str:
    return f"User({self.first_name},{self.last_name},{self.email})"
  
class WishlistItem(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.Text, nullable=False)
  company = db.Column(db.Text, nullable=False)
  source_url = db.Column(db.Text, nullable=False, unique=True)
  image_url = db.Column(db.Text, nullable=False, default="default.png")
  date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  source_name = db.Column(db.Text, nullable=False)
  job_type = db.Column(db.Text, nullable=False, default="Unknown")
  user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
  
  def __repr__(self) -> str:
    return f"WishlistItem({self.user_id},{self.id})" 