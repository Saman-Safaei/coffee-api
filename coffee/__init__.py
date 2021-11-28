from coffee.src.core import FlaskApp
from coffee.src.core.extensions import db
from coffee.src.core.extensions import api
from . import config


def create_app():
    app = FlaskApp(
        __name__,
        template_folder=config.TEMPLATES_DIR
    )
    app.config.from_pyfile(config.__file__)

    app.install_blueprints()
    app.install_all_api()

    db.init_app(app)
    api.init_app(app)

    return app
