from odoo import api, fields, models

class Course(models.Model):
    _name="academy.course"
    _description="Course Info"
    

    name=fields.Char(string="Title", required=True)
    active=fields.Boolean(string="Active",default=True)

    description = fields.Text()
    level= fields.Selection(string="Level",
                            selection=[
                                ('beginner','Beginner'),
                                ('intermediate','Intermediate'),
                                ('advanced','Advanced',)
                            ],
                            copy=False)
    
    session_ids=fields.One2many(comodel_name="academy.session", string="Sessions",inverse_name="course_id")