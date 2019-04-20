from faker import Faker
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

app = Flask('sayhello')
app.config.from_pyfile('settings.py')  # 加载配置
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
fake = Faker()
from sayhello import commands, views, errors
