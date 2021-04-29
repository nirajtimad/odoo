# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class StudentCourse(models.Model):
    _name = 'student.course'
    _description = 'Student Course'
    _rec_name = 'course_name'

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_done(self):
        for rec in self:
            rec.state = 'inactive'

    @api.multi
    def write(self, vals):
        res = super(StudentCourse, self).write(vals)
        print('write done')
        return res

    student_name = fields.Char(string='Student Name')
    course_name = fields.Char(string='Course Name')
    course_duration = fields.Char(string='Course Duration')
    stream = fields.Many2one('school.student', 'stream', String='Stream')
    state = fields.Selection([
        ('confirm', 'Active'),
        ('inactive', 'Inactive'),

    ], string='Status', default='confirm', index=True, readonly=True)



