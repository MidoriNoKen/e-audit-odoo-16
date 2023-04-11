# -*- coding: utf-8 -*-
{
    'name': "eaudit",

    'summary': """
        Modul untuk audit""",

    'description': """
        Modul untuk audit dengan menggunakan Odoo ERP
    """,

    'author': "Kelompok 2 (Berita)",
    'website': "https://www.k2.com",

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
        'views/views.xml',
        'views/menu.xml',
        'views/templates.xml',
        'views/eaudit_auditdata.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'images': ['static/description/icon.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
}
