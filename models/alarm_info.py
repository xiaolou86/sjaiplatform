from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AlarmInfo(db.Model):
    __tablename__ = 'alarm_info'
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(200), nullable=False)
    severity = db.Column(db.String(20))
