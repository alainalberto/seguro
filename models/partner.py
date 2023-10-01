from odoo import fields, models, _
from odoo.addons.base.models.res_partner import WARNING_MESSAGE, WARNING_HELP


class ResPartner(models.Model):
     _name = 'res.partner'
     _inherit = 'res.partner'
     
     x_cliente_ssn = fields.Char(string="Social Security Number")