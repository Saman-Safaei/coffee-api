from flask import Blueprint


products_bp = Blueprint("products", __name__, url_prefix='/products/')


from . import models
from . import views
from . import urls
