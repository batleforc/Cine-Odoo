from odoo import models, fields, api

class EventSeance(models.Model):
  _inherit ="event.event"

  seance = fields.Many2one('om_cine.seance')