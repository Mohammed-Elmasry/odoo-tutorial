from odoo import models, fields

class Session(models.Model):
    _name = "openacademy.session"
    _description = "Openacademy Sessions"

    name = fields.Char(required=True)
    start_date = fields.Datetime()
    duration = fields.Float(digits=(6,2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")