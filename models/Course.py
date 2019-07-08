from odoo import models, fields

class Course(models.Model):
    _name = "openacademy.course"
    _description = "openAcademy courses"

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    responsible_id = fields.Man2one('res.partner', required=True,
                ondelete='set null', string="Responsible", index=True)
