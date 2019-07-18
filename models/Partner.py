from odoo import fields, models

class Partner(models.Model):
    _inherit = "res.partner"

    instructor = fields.Boolean("Instructor", default=False)
    category = fields.Selection([("teacher1","Teacher 1"),("teacher2"),"Teacher 2"])
    session_ids = fields.Many2many("openacademy.session",string="Attended sessions"
                                   , readonly=True)
