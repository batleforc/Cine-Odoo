from odoo import models, fields, api


class CineSite(models.Model):
    _name = 'om_cine.site'
    _description = 'om_cine.site'

    name = fields.Char(string="Site name", required=True)
    description = fields.Text()
    address = fields.Char(string="Addres du site")

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100