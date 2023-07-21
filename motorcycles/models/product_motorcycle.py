from odoo import api, fields, models

class ProductMotorcycle(models.Model):
    _inherit='product.template'

    detailed_type = fields.Selection(selection_add=[ ('motorcycle', 'Motorcycle'), ], 
                                     ondelete={'motorcycle': 'set product'})
    horsepower= fields.Float(string="Horsepower")
    top_speed = fields.Float(string="Top Speed")
    torque=fields.Float(string="Torque")
    battery_capacity=fields.Char(string="Battery Capacity")
    charge_time=fields.Float(string="Charge Time")
    m_range=fields.Float(string="Range")
    curb_weight=fields.Float(string="Curb Weight")
    year=fields.Integer(string="Year")
    make=fields.Char("Make")
    model=fields.Char("Model")
    launch_date=fields.Date("Launch Date")
    
    @api.onchange('detailed_type')
    def _detailed_type_mapping(self):
        type_mapping = super()._detailed_type_mapping()
        type_mapping['motorcycle'] = 'product'
        return type_mapping
    