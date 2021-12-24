from flask import Flask


class FlaskApp(Flask):
    __app = None

    def __new__(cls, *args, **kwargs):
        if cls.__app is None:
            cls.__app = super().__new__(cls)
        return cls.__app

    def install_blueprints(self):
        from coffee.src.site import site_bp
        self.register_blueprint(site_bp)

        from coffee.src.uploads import uploads_bp
        self.register_blueprint(uploads_bp)

    def install_all_api(self):
        from coffee.src import api_products

        from coffee.src.api_users import users_bp
        self.register_blueprint(users_bp)

    def init_database(self):
        from . import database_initializer

    @classmethod
    def get_app(cls) -> Flask:
        return cls.__app
