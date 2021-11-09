# -*- coding: utf-8 -*-
{
    'name': "om_cine",

    'summary': """Cine management software""",

    'description': """
        OH MY CINEMA
    """,

    'author': "Weebo",
    'website': "https://maxleriche.tech",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'web',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website'],
    'installable': True,
    'application': True,
    'auto_install': False,

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/cinema.xml',
        'views/templates.xml',
        'security/ir.model.access.csv'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
