import os


# Directory Paths
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOADS_DIR = os.path.join(BASE_DIR, "resources/uploads")
RES_DIR = os.path.join(BASE_DIR, "resources")

# Security Configurations
SECRET_KEY = "too-secret-dont-tell-anyone"

# Database Configurations
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "data.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False
JSON_AS_ASCII = False
