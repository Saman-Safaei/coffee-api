from .app import FlaskApp
from .extensions import db

app = FlaskApp.get_app()


@app.before_first_request
def before_first_request():
    db.create_all()
