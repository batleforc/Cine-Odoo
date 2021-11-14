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
    'depends': ['base','website','calendar'],
    'installable': True,
    'application': True,
    'auto_install': False,

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/cinema.xml',
        'views/film.xml',
        'views/salle.xml',
        'views/seance.xml',
        'views/site.xml',
        'views/templates.xml',
        'views/template_web/a_la_une.xml',
        'views/template_web/site_choix_seance.xml',
        'views/template_web/film_choix_site.xml',
        'views/template_web/a_la_une.xml',
        'security/ir.model.access.csv',
        'security/security.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
