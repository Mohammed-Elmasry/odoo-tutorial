from odoo import models, fields, api

class Session(models.Model):
    _name = "openacademy.session"
    _description = "Openacademy Sessions"

    name = fields.Char(required=True)
    start_date = fields.Datetime()
    duration = fields.Float(digits=(6,2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    instructor_id = fields.Many2one('res.partner', string="Instructor", domain=['|', ("instructor","=",True) \
                                                                                   , ('category','ilike','teacher')])
    course_id = fields.Many2one('openacademy.course', ondelete="cascade", string="Course",
                                required=True)

    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    taken_seats = fields.Float(string="Taken seats", compute="_taken_seats")

    @api.depends("attendee_ids", seats)
    def _taken_seats(self):
        for record in self:
            if not record.seats:
                record.seats = 0.0;
            else:
                record.taken_seats = 100.0 * len(record.attendee_ids) / record.seats