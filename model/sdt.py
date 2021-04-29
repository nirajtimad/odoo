# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.tools import float_round

class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    student_name = fields.Char(string='Student Name')
    student_age = fields.Integer('Age')


class StudentInfo(models.Model):
    _name = 'school.student'
    _description = 'Student Record'
    _rec_name = 'student_name'

    def action_confirm(self):
        for rec in self:
            # Search method
            student_male = self.env['school.student'].search([('gender', '=', 'male')])
            print(student_male)
            student_female = self.env['school.student'].search([('gender', '=', 'female')])
            print(student_female)

            # Search_count method
            student_count = self.env['school.student'].search_count([])
            print(student_count)

            # ref method
            stud_ste = self.env.ref('student.stream_form')
            print(stud_ste.id)
            rec.state = 'confirm'

            # browse method
            browse_res = self.env['school.student'].browse(1)
            print(browse_res)

            # exit method
            if browse_res.exists():
                print('valid')
            else:
                print('Invalid')

            # create method
            values = {
              'student_name': 'raja'
            }
            new_record = self.env['school.student'].create(values)
            print(new_record.id)

            # write method
            update = self.env['school.student'].browse(1)
            if update.exists():
                values = {
                    'student_name': 'ninja123'
                }
                update.write(values)
            # copy method
            record_copy = self.env['school.student'].browse(1)
            record_copy.copy()

    def action_done(self):
        for rec in self:
            rec.state = 'inactive'

    #@api.model
    #def create(self, vals_list):
     #   res = super(StudentInfo, self).create(vals_list)
      #  print('res', res)
       # print('vals_list',vals_list)
        #print('yes_working')
       # return res

    @api.multi
    def write(self, vals):
        res = super(StudentInfo, self).write(vals)
        print('write done')
        return res

    @api.multi
    def unlink(self):
        print('done', self)
        for rec in self:
            if rec.gender == 'female':
                super(StudentInfo, rec).unlink()
            else:
                raise UserError(_('You Cannot delete record'))

        return

    @api.multi
    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, '%s -' '%s' % (rec.student_name, rec.student_age)))
        return res

    @api.depends('marathi', 'hindi', 'english', 'total', 'percentage')
    def addition(self):
        total = self.marathi+self.hindi+self.english
        self.total = total
        percentage_cal = (self.total / 300) * 100
        self.percentage = round(percentage_cal)
        if self.percentage:
            if self.percentage >= 91:
                self.grade = 'A+'
            elif self.percentage<=90 and self.percentage>=70 :
                self.grade = 'A'
            elif self.percentage <= 69 and self.percentage >=50:
                self.grade = 'B'
            else:
                self.grade = 'C'
        if self.marathi <= 100:
            pass
        else:
            raise UserError(_('Marks not Greater than 100'))
        if self.hindi <= 100:
            pass
        else:
            raise UserError(_('Marks not Greater than 100'))
        if self.english <= 100:
            pass
        else:
            raise UserError(_('Marks not Greater than 100'))

    @api.onchange('student_age')
    def add_age(self):
        if self.student_age<=50 and self.student_age >= 30:
            pass
        else:
            raise UserError(_('Age between 30 to 50'))

    # @api.depends('total')
    # def percent(self):
    #     percentage_cal = (self.total/300)*100
    #     self.percentage = percentage_cal
    #
    # @api.depends('percentage')
    # def set_grade(self):
    #     if self.percentage:
    #         if self.percentage >= 91:
    #             self.grade = 'A+'
    #         elif self.percentage<=90 and self.percentage>=70 :
    #             self.grade = 'A'
    #         elif self.percentage <= 69 and self.percentage >=50:
    #             self.grade = 'B'
    #         else:
    #             self.grade = 'C'
    student_name = fields.Char(string='Name')
    student_age = fields.Integer(string='Age', track_visibility='onchange')
    student_number = fields.Char(string="Student Number", readonly=True, required=True, index=True, copy=False, default= lambda self: _('New'))
    notes = fields.Text(string='Notes')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], 'Gender')
    date_of_birth = fields.Date('Date')
    marathi = fields.Float(string='Marathi')
    hindi = fields.Float(string='Hindi')
    english = fields.Float(string='English')
    total = fields.Float(string='Total', compute='addition')
    percentage = fields.Float(string='Percentage', compute='addition')
    grade = fields.Selection([('A+', 'A+'), ('A', 'A'), ('B', 'B'), ('C', 'C')], 'Grade', compute='addition')

    stream = fields.One2many('student.course', 'stream', String='Stream')
    student_course = fields.Many2one(
        'student.course',

        string='Course')
    state = fields.Selection([
        ('confirm', 'Active'),
        ('inactive', 'Inactive'),

    ], string='Status', default='confirm', index=True, readonly=True)

    @api.model
    def create(self, vals):
        print('vals1', vals)
        if vals.get('student_number', 'New') == 'New':
            vals['student_number'] = self.env['ir.sequence'].next_by_code(
                'school.student.sequence') or _('New')
        result = super(StudentInfo, self).create(vals)
        print('result::', result)
        return result