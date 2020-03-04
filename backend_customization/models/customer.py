###########################################################
#
# Made to do customization in customer (res.partner)model add workflow
#
############################################################

from odoo import api, fields, models
from lxml import etree
import simplejson

class ResPartner(models.Model):
    _inherit = 'res.partner'

    state = fields.Selection([('draft','Draft'),('approved','Approved')],string="State",default='draft')

    @api.multi
    def to_approve(self):
    	self.write({'state':'approved'})

    #TODO: make all fields readonly in approved state, add this to only cusomer partner, without view
    @api.model
    def fields_view_get(self,view_id=None,view_type='form',toolbar=False,submenu=False):
        context = self._context
        
        '''Workaround to add field using etree and make fields readonly TODO: refactore it and it was incorrect'''

        res = super(ResPartner, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar,submenu=submenu)
        arch = etree.XML(res['arch'])
        if view_type == 'form':
            #print("<<<<<<<<<<<<<<<<<",self.state)
            if context.get('search_default_customer', False) == 1 :
                # res['fields']['state']['selection'] = "[('draft','Draft'),('approved','Approved')]"
                res['fields'].update({"state":
                    {'String':'Status' ,
                    'type':'Selection',
                    'selection':"[('draft','Draft'),('approved','Approved')]"}})
                

                #print("IIIIIIIIIIIIIIIIIII",res['fields'])
                for node in arch.xpath("//field"):
                    #print("RRRRRRRRRRRRRRRRRRRRRR",node)
                    node.set('readonly','1')
                res['arch'] = etree.tostring(arch)
        return res