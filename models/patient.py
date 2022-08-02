from odoo import api, fields, models, tools

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", 'mail.activity.mixin']
    _description = "Hospital Patient"

    name = fields.Char('Name', required=True)
    age = fields.Integer('Age', required=True)
    gender = fields.Selection(selection=[('male', 'Male'),
                                        ('female', 'Female'),
                                        ('other', 'Other')],
                                required=True, string='Gender',default='male')
    note = fields.Text(string='Description')
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                              ('done', 'Done'), ('cancel', 'Cancelled')], default='draft', string='Status')
