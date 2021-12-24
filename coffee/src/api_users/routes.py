from . import users_bp
from . import views

users_bp.add_url_rule("/register", view_func=views.VRegister.as_view("register"))
users_bp.add_url_rule("/login", view_func=views.VLogin.as_view("login"))
