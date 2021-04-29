# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Student',
    'version': '12.0',
    'summary': 'Student Information',
    'sequence': 15,
    'description': """
        Information Of Student
    """,
    'category': 'School Management',
    'website': '',
    'images': [],
    'depends': ['base', 'sale'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'wizards/student_wizard.xml',
        'reports/report.xml',
        'reports/student_record.xml',
        'data/sequence.xml',
        'data/demo_data.xml',
        'view/std.xml', 'view/student_course.xml', 'view/template.xml',
        'view/course.xml', 'view/student_female.xml',
        'view/student_male.xml', 'view/stream.xml'



    ],
    'demo': [

    ],
    'qweb': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False,

}
