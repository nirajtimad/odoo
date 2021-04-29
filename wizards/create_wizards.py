# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class StudentWizard(models.TransientModel):
    _name = "student.wizard1"
    _description = "Wizards"

    student_name = fields.Char(string='Student Name')
    course = fields.Many2one('student.course', string='Course Name')

    def user_add(self):
        vals = {
            'student_name': self.student_name,
            'student_course': self.course
        }
        self.env['school.student'].create(vals)
        print(vals)

    def delete_record(self):
        for rec in self:
            print('done333', rec)
            res = self.env['school.student'].search([('student_name', '=', rec.student_name)])
            print(res)
            print(rec.student_name)
            if res:
                res.unlink()

            else:
                raise UserError(_('Never delete record'))
        return




