from odoo import models, fields, api


class CineFilm(models.Model):
    _name = 'om_cine.film'
    _description = 'om_cine.film'

    name = fields.Char(string="Nom du Film", required=True)
    description = fields.Text()
    synopsis = fields.Text()
    fournisseurs = fields.Char(string="Fournisseurs du film")
    duree = fields.Char(string="La durée du film")
    sites = fields.Many2many(comodel_name='om_cine.site',relation='film_site_rel',column1='om_cine_site_id',column2='om_cine_film_id')
