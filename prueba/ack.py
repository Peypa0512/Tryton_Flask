from trytond.model import ModelSQL, ModelView, fields
from trytond.pool import Pool

class Prueba(ModelSQL, ModelView):
    'Prueba'
    __name__ = 'ack.prueba'

    fecha = fields.Date('Fecha')
    dedicacion = fields.Time('Dedicacion')
    tipo_tarea = fields.Char('Tipo Tarea')
    estado_tarea = fields.Char('Estado Tarea')
    tecnico = fields.Char('Tecnico')
    cliente = fields.Char('Cliente')
    tarea = fields.Char('Tarea')
    descripcion = fields.Text('Descripcion')
    editor_ver = fields.Char('Editar/Ver')

class Plan_trabajo(ModelSQL, ModelView):
    'Plan de Trabajo'
    __name__ = 'ack.plan'
    cliente = fields.Char('Cliente')
    tecnico = fields.Char('Tecnico')
    nombre = fields.Char('Nombre')
    from_date = fields.Date('Desde Fecha')
    from_hour = fields.Time('Hora')
    to_date = fields.Date('Hasta Fecha')
    to_hour = fields.Time('Hora')
    tipo = fields.Char('Tipo')
    prioridad = fields.Char('Prioridad')
    tiempo = fields.TimeDelta('Tiempo')
    dedicacion = fields.Char('Dedicacion')
    estado = fields.Char('Estado')


class Employee(ModelSQL, ModelView):
    'Empleados'
    __name__ = "ack.employee"
    name = fields.Char("Nombre")
    dni = fields.Char("DNI")

