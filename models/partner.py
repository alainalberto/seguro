# -*- coding: uft-8 -*-

from odoo import api, fields, models, _


class ResPartner(models.Model):
     _inherit = "res.partner"

     x_cliente_ssn = fields.Char(string="Social Security Number")
     x_cliente_ein = fields.Char(string="EIN")
     x_cliente_usdot = fields.Char(string="US_DOT")
     x_cliente_pin = fields.Char(string="US_DOT Pin")
     x_cliente_user = fields.Char(string="US_DOT User")
     x_cliente_pasw = fields.Char(string="US_DOT Password")
     x_cliente_secut_quest = fields.Char(string="Security questions")
     x_cliente_mc = fields.Char(string="MC")
     x_cliente_tdmv = fields.Char(string="TDMV")
     x_cliente_login = fields.Char(string="Login")
     x_cliente_pass = fields.Char(string="Pass")
     x_cliente_uin = fields.Char(string="UIN")
     x_cliente_taxid = fields.Char(string="TaxID")
