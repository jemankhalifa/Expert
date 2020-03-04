# -*- coding: utf-8 -*-

from odoo import  fields, models

class PosConfig(models.Model):
    _inherit = 'pos.config'

    ''' Add custom fields to POS configuration
    	Limit Discount and orders per POS 
    '''

    limit_discount = fields.Boolean(string='Limit Disount Amount')
    pos_discount_amount = fields.Float(string='Discount POS Limit')

    limit_orders= fields.Boolean(string='Limit Orders')
    min_orders = fields.Integer(string='Min Orders')
    max_orders = fields.Integer(string='Max Orders')
    
    


