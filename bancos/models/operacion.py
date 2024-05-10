# -*- coding "utf-8" -*-
from odoo import models, fields, api

class Operacion(models.Model):
    _name = 'banco.operacion'
    _description = 'Operaciones Bancarias'

    idoperacion = fields.Char(string='Operacion Bancaria', required=True)
    descripcion = fields.Text(string='Descripcion', required=True)
    operacion = fields.Selection(string='Operacion',
                                 selection=[('S','Suma'),
                                            ('R','Resta')
                                           ])
    estado = fields.Boolean(string='Activo', default=True)