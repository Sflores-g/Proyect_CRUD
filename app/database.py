from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String())
    apellidos = db.Column(db.String())
    fecha_nacimiento = db.Column(db.DateTime())
    lugar_nacimiento = db.Column(db.String())
    sexo = db.Column(db.String())
    titulo = db.Column(db.String())

    def __init__(self, nombres, apellidos, fecha_nacimiento, lugar_nacimiento, sexo, titulo ):
        self.nombres = nombres
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.lugar_nacimiento = lugar_nacimiento
        self.sexo = sexo
        self.titulo = titulo

    def __repr__(self):
        return f"<Usuario {self.nombres}>"


