from odoo import models, fields, api


class CineSite(models.Model):
    _name = 'om_cine.site'
    _description = 'om_cine.site'

    name = fields.Char(string="Nom du site", required=True)
    description = fields.Text()
    address = fields.Char(string="Adresse du site")
    salles = fields.One2many('om_cine.salle',"site")
    films = fields.Many2many(comodel_name='om_cine.film',relation='film_site_rel',column2='om_cine_site_id',column1='om_cine_film_id')

