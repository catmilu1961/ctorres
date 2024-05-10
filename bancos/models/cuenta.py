# -*- coding "utf-8" -*-
from odoo import models, fields, api

class Cuenta(models.Model):
    _name = 'banco.cuenta'
    _description = 'Tipos de Cuentas'

    idtipoCuenta = fields.Text(string='Id Tipo Cuenta', required=True)
    description = fields.Text(string='Nombre Tipo Cuenta', required=True)
    tipo_cuenta = fields.Selection(string='Tipo Cuenta',
                           selection=[('ahorro','Ahorros'),
                                      ('monetarios','Monetarios'),
                                      ('inversion','Inversion Plazo Fijo')
                                       ])
    estado = fields.Boolean(string='Activa', default=True)