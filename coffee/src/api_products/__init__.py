import datetime
import os

from flask import request, jsonify, current_app, make_response
from flask_restful import Resource

from coffee.src.core.extensions import api
from coffee.src.core.extensions import db
from coffee.src.core.utilities import get_percent
from . import models


class Products(Resource):

    def get(self):
        db.create_all()
        product_id = request.args.get("id", None)
        response_list = list()
        if not product_id:
            all_data = models.MProducts.query.all()
            for data in all_data:
                response_list.append({
                    "id": data.get_id(),
                    "name": data.name,
                    "image_url": data.image_url,
                    "description": data.description,
                    "price": data.price,
                    "category": data.category,
                    "discount": data.discount,
                    "off_price": data.off_price
                })
        else:
            single_data = models.MProducts.query.filter_by(_id=product_id).first_or_404()
            response = make_response({
                "id": single_data.get_id(),
                "name": single_data.name,
                "image_url": single_data.image_url,
                "description": single_data.description,
                "price": single_data.price,
                "discount": single_data.discount,
                "category": single_data.category,
                "off_price": single_data.off_price
            })
            response.content_type = "application/json; charset=utf-8"
            return response
        response = make_response(dict(data=response_list))
        response.content_type = "application/json; charset=utf-8"
        return response

    def post(self):
        info_data = request.get_json()
        image_file = request.files.get("image", None)
        filename = str(datetime.datetime.now().year) + str(datetime.datetime.now().month) + str(
            datetime.datetime.now().day) + str(datetime.datetime.now().hour) + str(
            datetime.datetime.now().minute) + str(datetime.datetime.now().second) + image_file.filename
        filename.replace(" ", "")
        name = info_data["name"]
        description = info_data["description"]
        price = info_data["price"]
        discount = info_data["discount"]
        category = info_data["category"]
        off_price = info_data["off_price"]
        url = "https://api-coffee-flask.herokuapp.com/uploads/" + filename

        if name is None or description is None or price is None or discount is None or off_price is None:
            return {"massage": "Info is not complete !", "code": 4}

        product = models.MProducts(name=name, image_url=url, description=description, price=price, off_price=off_price,
                                   discount=discount, category=category)
        try:
            db.session.add(product)
            db.session.commit()
            image_file.save(os.path.join(current_app.config["UPLOADS_DIR"], filename))
            massage = "The Product is saved !"
            code = 201
        except Exception as w:
            massage = "The Product is not saved :" + str(w)
            code = 503

        return dict(massage=massage, code=code), code

    def delete(self):
        item_id = request.get_json()["item_id"]
        product = models.MProducts.query.filter_by(_id=item_id).first()
        if product is not None:
            product.delete()
            db.session.commit()
            return jsonify(dict(massage="Item Deleted", code=200)), 201
        else:
            return jsonify(dict(massage="This item is not exists", code=404)), 404

    def put(self):
        # Get Data from request
        update_info = request.get_json()
        # Get image file from request and set the filename
        image_file = request.files.get("image", None)
        filename = str(datetime.datetime.now().year) + str(datetime.datetime.now().month) + str(
            datetime.datetime.now().day) + str(datetime.datetime.now().hour) + str(
            datetime.datetime.now().minute) + str(datetime.datetime.now().second) + image_file.filename
        # assign data values to variables
        _id = update_info["_id"]
        name = update_info["name"]
        description = update_info["description"]
        price = update_info["price"]
        discount = update_info["discount"]
        category = update_info["category"]
        url = "https://api-coffee-flask.herokuapp.com/uploads/" + filename

        if name is None or description is None or price is None or discount is None or category is None:
            return {"massage": "Info is not complete !", "code": 1}

        # get the model and update it from database
        product = models.MProducts.query.filter_by(_id=_id).first()
        if product is None:
            return {"massage": "This item is not exists", "code": 404}, 404
        product.name = name
        product.description = description
        product.image_url = url
        product.price = price
        product.category = category
        product.discount = discount
        product.off_price = get_percent(price, discount)

        try:
            db.session.commit()
            return {"massage": "The Item has been updated.", "code": 201}, 201
        except Exception as e:
            return {"massage": str(e), "code": 503}, 503


api.add_resource(Products, "/products")
