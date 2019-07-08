from odoo import models, fields

class Course(models.Model):
    _name = "openacademy.course"
    _description = "openAcademy courses"

    name = fields.Char(string="Title", required=True)
    description = fields.Text()

