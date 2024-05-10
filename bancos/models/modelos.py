# -*- coding "utf-8" -*-
from odoo import models, fields, api

class aparcamiento(models.Model):
    _name = 'garaje.aparcamiento'
    _description = 'Permite definir las caracteristicas de un aparcamiento'
    
    name = fields.Char('Direccion', required=True)
    plazas = fields.Integer(string='Plazas', required=True)
    
    #relacion entre tablas
    coche_ids = fields.One2many(comodel_name='garaje.coche',
                                inverse_name='aparcamiento_id', 
                                string='Vehiculos')

class coche(models.Model):
    _name = 'garaje.coche'
    _description = 'Permite definir las caracteristicas de un coche'
    _order = 'name'
     
    name = fields.Char(string='Matricula', required=True, size=7)
    modelo = fields.Char(string='Modelo', required=True)
    construido = fields.Date(string='Fecha de construccion')
    consumo = fields.Float(string='Cosumo', 
                           default=0.0,
                           help='Consumo promedio cada 100 kms')
    #store=True no es conveniente en este caso
    annos = fields.Integer('Años', compute='_get_annos')
    descripcion = fields.Text('Descripcion')
    
    #relaciones entre tablas
    aparcamiento_id = fields.Many2one('garaje.aparcamiento', string='Aparcamiento')
    mantenimiento_ids = fields.Many2many('garaje.mantenimiento', string='Mantenimientos')
    
    @api.depends('construido')
    def _get_annos(self):
        #TODO: lo dejamos para mas adelante
        for coche in self:
            coche.annos = 0
            
          
class mantenimiento(models.Model):
    _name = 'garaje.mantenimiento'
    _description = 'Permite definir mantenimientos rutinarios sobre conjuntos de coches'
    _order = 'fecha'
    
    #name = fields.Char()
    fecha = fields.Date('Fecha', required=True, default=fields.date.today())
    tipo = fields.Selection(string='Tipo', 
                            selection=[('l','Lavar'),
                                       ('r','Revision'),
                                       ('m','Mecanica'),
                                       ('p','Pintura')
                                       ], default='l')
    coste = fields.Float('Coste', 
                         help='Coste total del mantenimiento')
    
    #relaciones entre tablas
    coche_ids = fields.Many2many('garaje.coche', string='Coches')