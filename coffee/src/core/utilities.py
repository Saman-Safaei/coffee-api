from flask import make_response


def get_percent(num, percent):
    if percent > 100:
        raise ValueError()
    percentage = (num / 100) * percent
    return percentage


def make_api_response(data, *args):
    response = make_response(data, *args)
    response.content_type = "application/json; charset=utf-8"
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response
