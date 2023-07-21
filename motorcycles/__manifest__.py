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
    'depends': ['stock','base'],
    'data': [
        'security/registry_groups.xml',
        'security/ir.model.access.csv',
        'data/registration_data.xml',
        'views/motorcycle_menuitems.xml',
        'views/motorcycle_views.xml',
        'views/product_views_inherit.xml',
        'views/compare_web_template.xml',
    ],
    'demo': [
    ],
    'application': True,

}