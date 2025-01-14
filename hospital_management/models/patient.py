from odoo import api,  fields, models


class HospitalPatient (models.Model):
    _name = "hospital.patient"
    _description="Patient Master Data"
    _inherit=['mail.thread']

    name = fields.Char(string="Name", required=True, tracking=True)
    date_of_birth = fields.Date(string="DOB")
    gender = fields.Selection ([('male', 'Male'), ('female','Female')],string="Gender")


