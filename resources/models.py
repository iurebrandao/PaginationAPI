from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Wine(db.Model):
    __tablename__ = 'wine'
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(128))
    description = db.Column(db.String(128))
    designation = db.Column(db.String(128))
    points = db.Column(db.Integer)
    price = db.Column(db.Float)
    province = db.Column(db.String(255))
    region_1 = db.Column(db.String(255))
    region_2 = db.Column(db.String(255))
    taster_name = db.Column(db.String(255))
    taster_twitter_handle = db.Column(db.String(255))
    title = db.Column(db.String(255))
    variety = db.Column(db.String(255))
    winery = db.Column(db.String(255))
