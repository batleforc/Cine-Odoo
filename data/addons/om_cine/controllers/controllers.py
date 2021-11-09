# -*- coding: utf-8 -*-
# from odoo import http


# class OmCine(http.Controller):
#     @http.route('/om_cine/om_cine/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/om_cine/om_cine/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('om_cine.listing', {
#             'root': '/om_cine/om_cine',
#             'objects': http.request.env['om_cine.om_cine'].search([]),
#         })

#     @http.route('/om_cine/om_cine/objects/<model("om_cine.om_cine"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('om_cine.object', {
#             'object': obj
#         })
