from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS


db = SQLAlchemy()
api = Api(prefix="/api/")
cors = CORS(resources={r"/api/*": {"origins": "*"}})
