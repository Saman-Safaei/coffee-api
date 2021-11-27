from . import views
from . import uploads_bp


uploads_bp.add_url_rule('/<string:filename>', view_func=views.VUploaded.as_view("uploaded"))
