# 数据库建模
from datetime import datetime

from sayhello._init_ import db


class Message(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    message = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.now, index=True)
