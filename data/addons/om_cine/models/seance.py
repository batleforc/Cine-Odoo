from odoo import models, fields, api


class CineSeance(models.Model):
    _name = 'om_cine.seance'
    _description = 'om_cine.seance'

    horaire_depart = fields.Char(string="", required=True)
    horaire_fin = fields.Char(string="", required=True)

