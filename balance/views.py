from datetime import date

from flask import render_template, request

from . import app
from .forms import MovimientosForm
from .models import DBManager


RUTA = 'data/balance.db'


@app.route("/")
def inicio():
    """
    Muestra la lista de movimientos cargados.
    """
    db = DBManager(RUTA)
    movimientos = db.consultaSQL("SELECT id, fecha, concepto, tipo, cantidad FROM movimientos")
    return render_template("inicio.html", movs=movimientos)


@app.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    return render_template("nuevo.html")


@app.route("/modificar/<int:id>", methods=["GET", "POST"])
def actualizar(id):
    if request.method == "GET":
        db = DBManager(RUTA)
        movimiento = db.obtenerMovimientoPorId(id)
        print("ANTES:", movimiento["fecha"])
        movimiento["fecha"] = date.fromisoformat(movimiento["fecha"])
        print("DESPUÉS:", movimiento["fecha"])
        
        formulario = MovimientosForm(data=movimiento)
        return render_template("form_movimiento.html", form=formulario)   


@app.route("/borrar/<int:id>", methods=["GET", "POST"])
def eliminar(id):
    db = DBManager(RUTA)
    esta_borrado = db.borrar(id)
    return render_template("borrar.html", resultado=esta_borrado)        