from coffee.src.core import FlaskApp
from coffee.src.core.extensions import db
from . import config


def create_app():
    app = FlaskApp(__name__)
    app.config.from_pyfile(config.__file__)

    app.install_blueprints()

    db.init_app(app)

    return app
