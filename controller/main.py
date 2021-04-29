from odoo import http
from odoo.http import request


class School(http.Controller):

    @http.route('/school_male', type='http', auth='public')
    def studentmale(self, **kw):
        male = request.env['school.student'].sudo().search([('gender', '=', 'male')])
        print('student:', male)
        return request.render('student.male', {
            'students': male
        })

    @http.route('/school_female', type='http', auth='none')
    def studentfemale(self, **kw):

        female = request.env['school.student'].sudo().search([('gender', '=', 'female')])
        print('student:', female)
        return request.render('student.female', {
            'students': female
        })

    @http.route('/school_student', type='http', auth='none')
    def student(self, **kw):
        students = request.env['school.student'].sudo().search([])
        print('student:', students)
        return request.render('student.student_page', {
            'students': students
        })

    @http.route('/student_course', type='http', auth='none')
    def course(self, **kw):
        courses = request.env['student.course'].sudo().search([])
        print('student:', courses)
        return request.render('student.student_page1', {
            'courses': courses
        })
