class Config:
    # clase de configuración de flask
    SECRET_KEY = "cosas secretas"
    SQLALCHEMY_DATABASE_URI = "postgresql://<nombre_usuario>:<password>@<host>:<puerto>/<nombre_basededatos>"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

