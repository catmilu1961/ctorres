# -*- coding "utf-8" -*-
{
    'name': 'Bancos',
    'description': 'Manejo de Operaciones Bancarias',
    'version': '0.1',
    'author': 'CT-Ideas-SOFT',
    'website': 'https://www.odoo.com',
    'license': 'LGPL-3',
    'category': 'Accounting',
    'depends': ['base'],
    'data': [
         'security/banco_seguridad.xml',
         'security/ir.model.access.csv',   
         'views/banco_menu_items.xml',
         'views/banco_views.xml',
         'views/cuenta_views.xml',
         'views/persona_views.xml',
         'views/operacion_views.xml',
         'views/aparcamiento_views.xml',
         'views/coche_views.xml',
         'views/mantenimiento_views.xml',
    ],
    'demo': [

    ],
    'installable': True,
    'auto_install': True,
}
