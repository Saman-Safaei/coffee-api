from coffee.src.core.extensions import db


class MUser(db.Model):
    __tablename__ = "users"

    _id = db.Column(db.INTEGER(), primary_key=True, autoincrement=True)
    f_name = db.Column(db.VARCHAR(40), nullable=False)
    l_name = db.Column(db.VARCHAR(40), nullable=False)
    username = db.Column(db.VARCHAR(80), nullable=False, unique=True)
    password = db.Column(db.VARCHAR(80), nullable=False)
    phone_number = db.Column(db.VARCHAR(30), nullable=False, unique=True)
    e_mail = db.Column(db.VARCHAR(80), nullable=False, unique=True)
    is_admin = db.Column(db.BOOLEAN(), default=False, nullable=False)

    def __init__(self, f_name, l_name, username, password, phone_number, e_mail, is_admin=False):
        self.f_name = f_name
        self.l_name = l_name
        self.username = username
        self.password = password
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.is_admin = is_admin
