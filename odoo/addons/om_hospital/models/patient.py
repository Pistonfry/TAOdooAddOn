from odoo import api, fields, models

class HospitalPatients(models.Model):
    _name = "hospital.patients" 

    name = fields.Char(string='Name', required=True)
    age=fields.Integer(string="Age")
    is_child=fields.Boolean(string="Is Child ?")
    notes=fields.Text(string="Notes")
    gender=fields.Selection([('male','Male'),('female','Female'),('others','Others')], string="Gender")
    