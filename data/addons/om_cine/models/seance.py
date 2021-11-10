from odoo import models, fields, api


class CineSeance(models.Model):
    _name = 'om_cine.seance'
    _description = 'om_cine.seance'

    name = fields.Char(compute="_get_name")
    horaire_depart = fields.Datetime(string="Horaire de début", required=True)
    horaire_fin = fields.Datetime(string="Horaire de fin", required=True)
    site_id = fields.Many2one('om_cine.site', required=True)
    salle = fields.Many2one('om_cine.salle', domain="[('site','=',site_id)]", required=True)
    film = fields.Many2one('om_cine.film', domain="[('sites','=',site_id)]" ,required=True)
    event = fields.Many2one('event.event',required=True)
    salle_name = fields.Char(string="Nom de la salle", tracking=True, related="salle.name")
    site_name = fields.Char(string="Nom du site", tracking=True, related="site_id.name")
    film_name = fields.Char(string="Nom du film", tracking=True, related="film.name")

    @api.onchange('salle_name','site_name','film_name')
    def _get_name(self):
        try:
            self.name= "{0}:{1}-{2}".format(self.site_name,self.salle_name,self.film_name)
        except:
            self.name= "ERROR NAMING THE FIELD"
