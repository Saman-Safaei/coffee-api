from coffee.src.core import error_codes, error_massages as em
from coffee.src.core.extensions import db

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
            return jsonify(dict(massage="Info is not complete", code=error_codes.data_incomplete))

        # Check database variables
        exists_username = models.MUser.query.filter_by(username=username).first()
        exists_email = models.MUser.query.filter_by(e_mail=e_mail).first()
        exists_phone = models.MUser.query.filter_by(phone_number=phone_number).first()

        if exists_username:
            # Make and return response for username
            return jsonify(dict(massage=em.username_already_exists, code=error_codes.username_already_exists)), 400
        if exists_email:
            # Make and return response for email
            return jsonify(dict(massage=em.email_already_exists, code=error_codes.email_already_exists)), 400
        if exists_phone:
            # Make and return response for phone number
            return jsonify(dict(massage=em.phone_already_exists, code=error_codes.phone_already_exists)), 400

        # create and commit user
        user = models.MUser(f_name, l_name, username, password, phone_number, e_mail)

        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            # Make and return response
            return jsonify(dict(massage=em.an_error_occurred + str(e), code=error_codes.an_error_occurred)), 503

        # Make and return response
        return jsonify(
                dict(
                    user=dict(firstName=user.f_name, lastName=user.l_name,
                              userName=user.username,
                              email=user.e_mail, phoneNumber=user.phone_number),
                    code=201)), 201


# ----------------------------------------------------------------------------------------------------------------------


class VLogin(View):
    methods = ["POST"]

    def dispatch_request(self):
        data = request.get_json()
        username = data.get("userName")
        password = data.get("password")

        if not username or not password:
            return jsonify(dict(massage=em.data_incomplete, code=error_codes.data_incomplete))

        user = models.MUser.query.filter_by(username=username).first()

        if not user:
            return jsonify(dict(massage=em.user_not_found, code=error_codes.user_not_found))

        user_password = user.password

        if user_password != password:
            return jsonify(dict(massage=em.wrong_password, code=error_codes.wrong_password))

        return jsonify(dict(
                user=dict(
                    userName=user.username,
                    email=user.e_mail,
                    firstName=user.f_name,
                    lastName=user.l_name,
                    phoneNumber=user.phone_number
                ), code=200))
