# -*- coding "utf-8" -*-
from odoo import models, fields, api

class Banco(models.Model):
    _name = 'banco.bancos'
    _description = 'Catalogo de Bancos'

    idbanco = fields.Char(string='Sigla Banco:', required=True)
    descripcion = fields.Text(string='Nombre Banco:', required=True)
    estado = fields.Boolean(string='Activo:', default=True)