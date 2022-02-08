from .database import *

def create_db():
    """creanción de la base de datos"""
    db.drop_all()
    db.create_all()


    """inicialización de la base de datos"""

def init_db():

    create_db()

    # admin = Usuario(
    #     nombres = "Sandra",
    #     apellidos = "Flores",
    #     fecha_nacimiento = "31/8/1991",
    #     lugar_nacimiento = "Iquitos",
    #     sexo = "femenino",
    #     titulo = "Sistemas",
    # )
    # db.session.add(admin)
    # db.session.commit()