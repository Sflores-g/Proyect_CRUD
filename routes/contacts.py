from flask import Blueprint, flash, render_template, request, redirect, jsonify, url_for, json
from app.database import Usuario
from app.database import *




contacts = Blueprint("contacts",__name__)



@contacts.route("/")
def index():
    contacts = Usuario.query.all()

    return render_template("index.html", contacts=contacts)


@contacts.route("/new", methods=["POST"])
def add_usuarios():

    if request.method == 'POST':

        nombres = request.form["nombres"]
        apellidos = request.form["apellidos"]
        fecha_nacimiento = request.form["fecha_nacimiento"]
        lugar_nacimiento = request.form["lugar_nacimiento"]
        sexo = request.form["sexo"]
        titulo = request.form["titulo"]

        new_usuario = Usuario(nombres, apellidos, fecha_nacimiento, lugar_nacimiento, sexo, titulo )

        
        db.session.add(new_usuario)
        db.session.commit()
        
        flash("Se Creo usuario correctamente!")
        
        return redirect(url_for("contacts.index"))

@contacts.route("/actualizar/<id>", methods =["POST", "GET"])
def actualizar(id):
    contact = Usuario.query.get(id)

    if request.method == "POST":

        contact.nombres = request.form["nombres"]
        contact.apellidos = request.form["apellidos"]
        contact.fecha_nacimiento = request.form["fecha_nacimiento"]
        contact.lugar_nacimiento = request.form["lugar_nacimiento"]
        contact.sexo = request.form["sexo"]
        contact.titulo = request.form["titulo"]

        db.session.commit()

        flash("Se actualizó usuario correctamente!")

        return redirect(url_for("contacts.index"))

    return render_template("update.html", contact=contact)


@contacts.route("/eliminar/<id>")
def eliminar(id):
    contact = Usuario.query.get(id)
    db.session.delete(contact)
    db.session.commit()

    flash("Se Eliminó usuario correctamente!")

    return redirect(url_for("contacts.index"))