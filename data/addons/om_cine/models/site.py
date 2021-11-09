from odoo import models, fields, api


class CineSite(models.Model):
    _name = 'om_cine.site'
    _description = 'om_cine.site'

    name = fields.Char(string="Nom du site", required=True)
    description = fields.Text()
    address = fields.Char(string="Adresse du site")
    salles = fields.One2many('om_cine.salle',"site")

