from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler

# Initialize extensions
db = SQLAlchemy()
scheduler = APScheduler()

