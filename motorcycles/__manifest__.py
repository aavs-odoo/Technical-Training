{
    'name': 'Motorcycle Registry',
    'summary':"""Manage Registration of Motorcycles""",
    'description': """Motorcycle Registry
    ====================
    his Module is used to keep track of the 
    Motorcycle Registration and Ownership of 
    each motorcycled of the brand.
    """,
    'license': 'OPL-1',
    'author': 'aavs-odoo',
    'website': 'www.github.com/aavs-odoo.com',
    'category': 'Custom Modules/Kawiil',
    'depends': ['base'],
    'data': [
        'security/registry_groups.xml',
        'security/ir.model.access.csv',
        'views/motorcycle_menuitems.xml',
        'views/motorcycle_views.xml'
    ],
    'demo': [
        'demo/motorcycle_demo.xml'
    ],
    'application': True,

}