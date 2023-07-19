from odoo import fields, models

class Motorcycler(models.Model):
    _name="motorcycle.registry"
    _description="Motorcycles Registration"
    _rec_name="registry_number"

    registry_number=fields.Char(string="Registry Number", required=True)
    vin=fields.Char(string="Vin",required=True)
    first_name=fields.Char(string="Name",required=True)
    last_name=fields.Char(string="Last Name",required=True)
    picture=fields.Image(string="Image")
    current_mileage=fields.Float(string="Mileage")
    license_plate=fields.Char(string="License Plate")
    certificate_title=fields.Binary(string="Certificate")
    register_date=fields.Date(string="Date")