import time
import logging

from psycopg2 import sql, DatabaseError

from odoo import api, fields, models, _
from odoo.osv import expression
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT, mute_logger
from odoo.exceptions import ValidationError, UserError
from odoo.addons.base.models.res_partner import WARNING_MESSAGE, WARNING_HELP

class ResPartner(models.Model):
     _name = 'res.partner'
     _inhert = ['partner']

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
