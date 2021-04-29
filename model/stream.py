# -*- coding: utf-8 -*-

from odoo import models, fields


class StudentInfo(models.Model):
    _name = 'stream.student'
    _description = 'Student Record'
    _rec_name = 'stream_name'

    stream_name = fields.Char(string='Stream Name')
    student_name = fields.Char(string='Student Name')
    student_age = fields.Integer(string='Student age')

    state = fields.Selection([
        ('confirm', 'Active'),
        ('inactive', 'Inactive'),

    ], string='Status', default='confirm', index=True, readonly=True)