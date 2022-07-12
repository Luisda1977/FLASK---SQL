from random import choices
from flask_wlf import Flaskform
from wtform import Datefield, DecimalField, HiddenField, RadioField, StringField, Submitfield


class MovimientosForm(Flaskform):
    id = HiddenField()
    fecha = Datefield("Fecha")
    concepto = StringField("Concepto")
    tipo = RadioField(choices=[("I", "Ingreso"), ("G", "Gasto")])
    cantidad = DecimalField("Cantidad", places=2)

    submit = Submitfield("Guardar")
