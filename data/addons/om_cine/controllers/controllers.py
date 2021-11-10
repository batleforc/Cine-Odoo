# -*- coding: utf-8 -*-
from odoo import http

class OmCine(http.Controller):
    @http.route('/a_la_une', auth='public', website=True)
    def index(self, **kw):
        Films = http.request.env['om_cine.film']
        return http.request.render('om_cine.index', {
            'films': Films.search([])
        })
