from odoo import models, fields, api, exceptions
from datetime import datetime

class Session(models.Model):
    _name = "openacademy.session"
    _description = "Openacademy Sessions"

    name = fields.Char(required=True)
    start_date = fields.Datetime(default=datetime.today().strftime("%Y-%m-%d"))
    duration = fields.Float(digits=(6,2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    instructor_id = fields.Many2one('res.partner', string="Instructor", domain=['|', ("instructor","=",True) \
                                                                                   , ('category','ilike','teacher')])
    course_id = fields.Many2one('openacademy.course', ondelete="cascade", string="Course",
                                required=True)

    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    taken_seats = fields.Float(string="Taken seats", compute="_taken_seats")

    active = fields.Boolean(string="active", default=True)

    @api.depends("attendee_ids", "seats")
    def _taken_seats(self):
        for record in self:
            if not record.seats:
                record.seats = 0.0;
            else:
                record.taken_seats = 100.0 * len(record.attendee_ids) / record.seats

    @api.onchange("attendee_ids", "seats")
    def _verify_valid_seats(self):
        if self.seats < 0:
            self.seats = 0
            return {
                'warning':{
                    'title':"Incorrect 'seats' value",
                    'message':"The number of seats cannot be negative"
                }
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning' :{
                    'title':"Too Many Attendees",
                    'message':"Increase number of seats or remove excess attendees"
                }
            }

    # api.constrains work much as onsave() not onchange()
    @api.constrains("instructor_id","attendee_ids")
    def _check_instructor_not_in_attendee(self):
        for record in self:
            if record.instructor_id and record.instructor_id in self.attendee_ids:
                raise exceptions.ValidationError("A sessions's instructor cannot be an attendant")