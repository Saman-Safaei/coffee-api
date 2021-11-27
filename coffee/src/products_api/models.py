from coffee.src.core.extensions import db


class MProducts(db.Model):
    _id = db.Column(db.INTEGER(), primary_key=True, autoincrement=True)
    name = db.Column(db.VARCHAR(80), nullable=False)
    image_url = db.Column(db.VARCHAR(), nullable=False)
    description = db.Column(db.TEXT(), nullable=False)
    price = db.Column(db.INTEGER(), nullable=False)
    discount = db.Column(db.INTEGER(), nullable=False, default=False)
    off_price = db.Column(db.INTEGER(), nullable=False, default=0)

    def get_id(self):
        return self._id
