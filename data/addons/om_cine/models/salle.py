# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CineSalle(models.Model):
    _name="om_cine.salle"
    _description="om_cine.salle"

    name = fields.Char(string="Salle name",required=True)
    place= fields.Integer(string="Nombre de place", required=True)
    climatise = fields.Boolean(string="Climatisé")
    troisd = fields.Boolean( string="3D")