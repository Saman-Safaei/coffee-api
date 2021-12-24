from flask.views import View
from flask import send_from_directory, current_app


class VUploaded(View):
    def dispatch_request(self, **kwargs):
        filename = kwargs.get("filename")
        return send_from_directory(current_app.config["UPLOADS_DIR"], filename)
