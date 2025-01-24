from odoo import api,  fields, models


class HospitalAppointment (models.Model):
    _name = "hospital.appointment"
    _description="Patient Appointment Master Data"
    _inherit=['mail.thread']


    patient_id = fields.Many2one('hospital.patient', string="Patient")
    date_appointment = fields.Date(string="Date")
    Notes = fields.Text(string="Notes")

    name = fields.Char(string="Name", required=True, tracking=True)
    date_of_birth = fields.Date(string="DOB")
    gender = fields.Selection ([('male', 'Male'), ('female','Female')],string="Gender")


