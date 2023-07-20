from odoo import api,fields, models
from odoo.exceptions import ValidationError
import re

class Motorcycler(models.Model):
    _name="motorcycle.registry"
    _description="Motorcycles Registration"
    _rec_name="registry_number"

    registry_number=fields.Char(string="Registry Number", default="MRN0000",copy=False,required=True,readonly=True)
    vin=fields.Char(string="Vin",required=True)
    first_name=fields.Char(string="Name")
    last_name=fields.Char(string="Last Name")
    picture=fields.Image(string="Image")
    current_mileage=fields.Float(string="Mileage")
    license_plate=fields.Char(string="License Plate")
    certificate_title=fields.Binary(string="Certificate")
    register_date=fields.Date(string="Registration Date")

    owner_id= fields.Many2one(comodel_name="res.partner",string="Owner")
    email=fields.Char(related="owner_id.email")
    phone=fields.Char(related="owner_id.phone")

    brand=fields.Char(string="Brand", compute="_compute_separation_vin",readonly=False)
    make=fields.Char(string="Make", compute="_compute_separation_vin",readonly=False)
    model=fields.Char(string="Model", compute="_compute_separation_vin",readonly=False)
   




    _sql_constraints=[('unique_vin','UNIQUE (vin)','There can not be a duplicate Vin')]

    @api.model_create_multi
    def create(self,vals_list):
        for vals in vals_list:
            if vals.get('registry_number', ('MRN0000')) == ('MRN0000'):
                vals['registry_number']=self.env['ir.sequence'].next_by_code('registry.number')
        return super().create(vals_list)
    
    @api.constrains('vin')
    def _check_vin(self):
        for motorcycler in self:
            regex=r'^[A-Z]{2}[A-Z]{2}[0-9]{2}[A-Z|0-9]{2}[0-9]{6}$'
            if(re.match(regex,motorcycler.vin)==None):
                raise ValidationError ('Invalid Vin Format check again please.')

    @api.constrains('license_plate')
    def _check_license(self):
        for motorcycler in self:
            regex=r'^([A-Z]{1,4}[0-9]{1,3})([A-Z]{0,2})?$'
            if(re.match(regex,motorcycler.license_plate)==None):
                raise ValidationError ('Invalid License Format check again please.')
    

    @api.depends('vin')
    def _compute_separation_vin(self):
        for motorcycler in self:
            if(motorcycler.vin is not False and not motorcycler.vin == ""):    
                motorcycler.brand= motorcycler.vin[0:2]
                motorcycler.make= motorcycler.vin[2:4]
                motorcycler.model= motorcycler.vin[4:6]

