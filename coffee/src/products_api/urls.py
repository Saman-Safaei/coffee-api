from . import views, products_bp


products_bp.add_url_rule("/", view_func=views.VIndex.as_view("index"))
