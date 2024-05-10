# -*- coding "utf-8" -*-
from odoo import models, fields, api

class Persona(models.Model):
    _name = 'banco.persona'
    _description = 'Personas'

    dpi = fields.Char(string='DPI', required=True)
    nombres = fields.Text(string='Nombre', required=True)
    sexo = fields.Selection(string='Sexo',
                            selection=[('femenino','Femenino'),
                                       ('masculino','Masculino')
                                      ])
    edad = fields.Integer(string='Edad', required=True)
    estado = fields.Boolean(string='Activo', default=True)
    