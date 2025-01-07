from odoo import api, field, models


class HospitalPatient (models.Model):
    _name = "hospital.patient"


    name = fields.Char(string="Name", required=True)
    