from docutils.nodes import reference
from odoo import api, fields, models
from xlsxwriter.contenttypes import defaults


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _description = "Patient Appointment Master Data"
    _inherit = ['mail.thread']
    _rec_name = 'patient_id'

    reference = fields.Char(string="Reference", default="New")
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    date_appointment = fields.Date(string="Date", required=True)
    notes = fields.Text(string="Notes", required=True)


    @api.model_create_multi
    def create(self, vals_list):
        print("test", vals_list)
        for vals in vals_list:
            if not vals.get('reference') or vals['reference'] == 'New':
                vals['reference'] = self.env['ir.sequence'].next_by_code('hospital.appointment')
        return super().create(vals_list)