# -*- coding: utf-8 -*-
{
    'name': "eaudit",

    'summary': """
        eAudit adalah sebuah aplikasi yang digunakan untuk proses Audit Saya""",

    'description': """
        eaudit aplikasi berbasis Odoo ERP yang diimplementasikan di UIN Maulana Malik Ibrahim Malang
    """,

    'author': "UIN Maulana Malik Ibrahim Malang",
    'website': "https://uin-malang.ac.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/eaudit_auditdata.xml'
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
