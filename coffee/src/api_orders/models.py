from coffee.src.core.extensions import db


class MOrders(db.Model):
    __tablename__ = "orders"

    _id = db.Column(db.INTEGER(), primary_key=True, autoincrement=True)
    name = db.Column(db.VARCHAR(100), nullable=False)
    quantity = db.Column(db.INTEGER(), nullable=False)
    product_id = db.Column(db.INTEGER(), db.ForeignKey("products._id"))
    product = db.relation("MProducts", backref="orders", lazy=True)
    user_id = db.Column(db.INTEGER(), db.ForeignKey("users._id"))
    user = db.relation("MUser", backref="orders", lazy=True)

    is_paid = db.Column(db.BOOLEAN(), default=False, nullable=False)
