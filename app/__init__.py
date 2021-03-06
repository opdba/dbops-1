# encoding:utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)

    # 注册users蓝本
    from users.views import user_page
    app.register_blueprint(user_page, url_prefix='/user')

    return app
