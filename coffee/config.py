import os


# Directory Paths
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
RES_DIR = os.path.join(BASE_DIR, "resources")
UPLOADS_DIR = os.path.join(RES_DIR, "uploads")
TEMPLATES_DIR = os.path.join(RES_DIR, "templates")


# Security Configurations
SECRET_KEY = "too-secret-dont-tell-anyone"

# Database Configurations
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "data.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False
JSON_AS_ASCII = False
