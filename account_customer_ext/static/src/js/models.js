odoo.define( "account_customer_ext.models", function(require) {
    'use strict';
    var models = require('account.models');

    models.load_fields('res.partner', ['x_cliente_ssn', 'x_cliente_ein','x_cliente_usdot', 'x_cliente_pin', 'x_cliente_user', 'x_cliente_pasw', 'x_cliente_secut_quest', 'x_cliente_mc', 'x_cliente_tdmv', 'x_cliente_login', 'x_cliente_pass', 'x_cliente_uin']);
    
});