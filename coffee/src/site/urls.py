from . import views, site_bp


site_bp.add_url_rule("/", view_func=views.VIndex.as_view("index"))
