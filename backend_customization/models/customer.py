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

    #TODO: make all fields readonly in approved state, add this to only cusomer partner, without view
    @api.multi
    def to_approve(self):
    	self.write({'state':'approved'})

    @api.model
    def fields_view_get(self,view_id=None,view_type='form',toolbar=False,submenu=False):
    	context = self._context

    	res = super(ResPartner, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar,submenu=submenu)
    	doc = etree.XML(res['arch'])
    	if view_type == 'form':
    		print("<<<<<<<<<<<<<<<<<",self.state)
    		if context.get('search_default_customer', False) == 1 :
    			custom_view = self.env['ir.ui.view'].search([('id', '=', view_id)], limit=1)
    			result['fields'].update("n":{'String': , 'type':})
                for cu in custom_view:
    				print("_______________",cu)

	    		for node in doc.xpath("//field"):   # All the view fields to readonly
	    			print("RRRRRRRRRRRRRRRRRRRRRR",node)
	    			node.set('readonly' ,'1')
	    			node.set('modifiers',simplejson.dumps("{'readonly':true}"))
	    			print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$",node)
	    		res['arch'] = etree.tostring(doc)
    	# res = super(ResPartner,self).fields_view_get(view_id=view_id,view_type=view_type,toolbar=False,submenu=False)
    	# print("11111111111111111111111",res)
    	# if view_type == 'form':
    	# 	res['arch'] = self.fields_view_get(res['arch'])
    	# 	print("::::::::::::::::::::",res['arch'])
    		# doc = etree.XML(res['arch'])
    		# print("OOOOOOOOOOOOOOOOOOOOOOOOOO",doc)
    		# nodes = doc.xpath("//form")
    		# print("DSDSSSSSSSSSSSSSSSSSSSSSSSSSs",nodes)
    		# for nod in nodes:
    		# 	print("bbbbbbbbbbbbbbbbbb",nod)
	    		#nod.set(n, '{"readonly": true}')
	    		#{'name': {'readonly': False}}

    		# for n in res['fields']:
    		# 	f_attr = self.fields_get(n,'readonly')
    		# 	print(">>>>>>>>>>>>>>>>>>>>>>>>>",f_attr)
    		# 	f_attr.set(n, '{"readonly": true}')
    		# 	print("xxxxxxxxxxxxxxxxx",n)
    	return res