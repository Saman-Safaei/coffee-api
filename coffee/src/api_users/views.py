from coffee.src.core import error_codes, error_massages as em
from coffee.src.core.extensions import db
from coffee.src.core.utilities import make_api_response

from flask.views import View
from flask import jsonify
from flask import request

from . import models


class VRegister(View):
    methods = ["POST"]

    def dispatch_request(self):
        # Get Data From Request
        data = request.get_json()
        f_name = data.get("firstName")
        l_name = data.get("lastName")
        username = data.get("userName")
        password = data.get("password")
        e_mail = data.get("email")
        phone_number = data.get("phoneNumber")

        # Check variables if are None
        if not f_name or not l_name or not username or not password or not e_mail or not phone_number:
            return jsonify(dict(massage="Info is not complete"), code=error_codes.data_incomplete)

        # Check database variables
        exists_username = models.MUser.query.filter_by(username=username).first()
        exists_email = models.MUser.query.filter_by(e_mail=e_mail).first()
        exists_phone = models.MUser.query.filter_by(phone_number=phone_number).first()

        if exists_username:
            # Make and return response for username
            response = make_api_response(
                jsonify(dict(massage=em.username_already_exists, code=error_codes.username_already_exists))
            )
            return response
        if exists_email:
            # Make and return response for email
            response = make_api_response(
                jsonify(dict(massage=em.email_already_exists, code=error_codes.email_already_exists))
            )
            return response
        if exists_phone:
            # Make and return response for phone number
            response = make_api_response(
                jsonify(dict(massage=em.phone_already_exists, code=error_codes.phone_already_exists))
            )
            return response

        # create and commit user
        user = models.MUser(f_name, l_name, username, password, phone_number, e_mail)

        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            # Make and return response
            response = make_api_response(
                jsonify(dict(massage=em.an_error_occurred + str(e), code=error_codes.an_error_occurred)), 503
            )
            return response

        # Make and return response
        response = make_api_response(
            jsonify(
                dict(
                    user=dict(firstName=user.f_name, lastName=user.l_name,
                              username=user.username,
                              email=user.e_mail, phoneNumber=user.phone_number),
                    code=201)), 201
        )
        return response


# ----------------------------------------------------------------------------------------------------------------------


class VLogin(View):
    methods = ["POST"]

    def dispatch_request(self):
        data = request.get_json()

