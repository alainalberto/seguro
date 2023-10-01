from odoo import models, fields


class ResPartner(models.Model):
     _inherit = 'res.partner'

     x_cliente_ssn = fields.Char(string="Social Security Number")