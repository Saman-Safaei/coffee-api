from flask import Flask


class FlaskApp(Flask):
    __app = None

    def __new__(cls, *args, **kwargs):
        if cls.__app is None:
            cls.__app = super().__new__(cls)
        return cls.__app

    def install_blueprints(self):
        from coffee.src.products_api import products_bp
        self.register_blueprint(products_bp)

        from coffee.src.uploads import uploads_bp
        self.register_blueprint(uploads_bp)
