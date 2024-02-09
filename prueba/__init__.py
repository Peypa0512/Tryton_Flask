from trytond.pool import Pool

__all__ = ['register']

import ack


def register():
    Pool.register(
        ack.Prueba,
        ack.Plan_trabajo,
        ack.Employee,
        module='prueba', type_='model')
    Pool.register(
        module='prueba', type_='wizard')
    Pool.register(
        module='prueba', type_='report')
