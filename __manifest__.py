# -*- coding: utf-8 -*-
{
    'name': "dh_elearning_dependencies",

    'summary': """
        Odoo elearning dependencies additional modul""",

    'description': """
        add dependencies or pre-requisites feature on basic odoo elarning module
    """,

    'author': "_dinoherlambang_",
    'website': "https://instagram.com/_dinoherlambang_",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'tools',
    'version': '16.0',

    # any module necessary for this one to work correctly
    'depends': ['base','web','website_slides'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/course_views.xml',
        'views/templates.xml',
    ],
    'qweb': ['static/src/xml/*.xml'],
    'css': ['static/src/css/course.css'],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
