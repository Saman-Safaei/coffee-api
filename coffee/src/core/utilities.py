from flask import make_response


def get_percent(num, percent):
    if percent > 100:
        raise ValueError()
    percentage = (num / 100) * percent
    return percentage
