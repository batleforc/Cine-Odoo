from odoo import models, fields, api


class CineFilm(models.Model):
    _name = 'om_cine.film'
    _description = 'om_cine.film'

    name = fields.Char(string="nom du Film", required=True)
    description = fields.Text()
    synopsis = fields.Text()
    fournisseurs = fields.Char(string="fournisseurs du film")
    duree = fields.Char(string="la durée du film")
