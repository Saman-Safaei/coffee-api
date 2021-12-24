from flask import render_template
from flask.views import View


class VIndex(View):
    def dispatch_request(self):
        return render_template("home.html")
