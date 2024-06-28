# models/course.py
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Course(models.Model):
    _inherit = 'slide.channel'

    prerequisite_ids = fields.Many2many(
        'slide.channel',
        'course_prerequisite_rel',
        'course_id',
        'prerequisite_id',
        string='Prerequisites',
        help='Courses that must be completed before this course can be taken'
    )

    @api.constrains('prerequisite_ids')
    def _check_prerequisite_ids(self):
        for course in self:
            if course in course.prerequisite_ids:
                raise ValidationError('A course cannot be a prerequisite for itself.')

class Enrollment(models.Model):
    _inherit = 'slide.slide.partner'

    @api.model
    def create(self, values):
        slide = self.env['slide.slide'].browse(values['slide_id'])
        course = slide.channel_id
        user = self.env['res.users'].browse(values['user_id'])

        for prereq in course.prerequisite_ids:
            if not self.env['slide.slide.partner'].search([
                ('channel_id', '=', prereq.id),
                ('user_id', '=', user.id),
                ('completed', '=', True)
            ]):
                raise ValueError('You must complete the prerequisite courses before enrolling in this course.')

        return super(Enrollment, self).create(values)
