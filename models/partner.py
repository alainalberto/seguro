from odoo import models, fields


class ResPartner(models.Model):
     _inhert = 'res.partner'

     x_cliente_ssn = fields.Char(string="Social Security Number")