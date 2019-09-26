from flask import Flask
from importlib import import_module
import os
from models.flight import Flight
from models.product import Product
from models.search import Search

from extensions import db, ma, migrate
from blueprints import http_blueprints
from management.populate import populate_command


def create_app():
    app = Flask(__name__)
    app_env: str = os.environ.get('FLASK_ENV', 'development')

    if app_env == 'production':
        app.config.from_object('config.ProductionConfig')
    elif app_env == 'testing':
        app.config.from_object('config.TestingConfig')
    else:
        app.config.from_object('config.DevelopmentConfig')

    for blueprint in http_blueprints:
        import_module(blueprint.import_name)
        app.register_blueprint(blueprint)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    app.cli.add_command(populate_command)

    return app
