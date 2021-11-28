from flask import Blueprint


site_bp = Blueprint("site", __name__)


from . import models
from . import views
from . import urls
