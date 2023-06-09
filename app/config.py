import os
from app.creds import SECRET_KEY

class Config: 
    SECRET_KEY = SECRET_KEY
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    UPLOAD_FOLDER = os.path.join(
        os.getcwd(), 'app/static/uploads/')