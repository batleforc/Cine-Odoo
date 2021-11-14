# -*- coding: utf-8 -*-
from odoo import http

class OmCine(http.Controller):
    @http.route('/', auth='public', website=True)
    def a_la_une(self, **kw):
        Films = http.request.env['om_cine.film']
        return http.request.render('om_cine.index', {
            'films': Films.search([])[:5]
        })

    @http.route('/films', auth='public', website=True)
    def films(self, **kw):
        Films = http.request.env['om_cine.film']
        return http.request.render('om_cine.index', {
            'films': Films.search([])
        })


    @http.route('/sites', auth='public', website=True)
    def sites(self, **kw):
        FilmId = kw.get("FilmId")
        Sites = http.request.env['om_cine.site'].search([('films', 'in', [FilmId])])
        return http.request.render('om_cine.sites', {
            'sites': Sites, 'filmId': FilmId
        })

    @http.route('/seances', auth='public', website=True)
    def seances(self, **kw):
        FilmId = kw.get("FilmId")
        SiteId = kw.get("SiteId")
        Seances = http.request.env['om_cine.seance']
        Seances = Seances.search([('site_id.id', '=', SiteId),('film.id','=',FilmId)])
        return http.request.render('om_cine.seances', {
            'seances': Seances
        })
