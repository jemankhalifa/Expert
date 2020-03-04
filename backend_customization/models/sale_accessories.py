###########################################################
# Made to do customization in sale order, new model called product_accessory
############################################################

from odoo import api, fields, models

class productProduct(models.Model):
    _inherit = 'product.product'

    accessory_ids = fields.One2many('product.accessory','name',string="Accessories")

class productAccessory(models.Model):
    _inherit = 'product.template'
    _name = 'product.accessory'

    name = fields.Many2one('product.product',string="Product")
    accessory_qty = fields.Float(string="Quantity")
    sequence = fields.Char(string="Accessory sequence")


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    sequence_no = fields.Char(string="No.")

    @api.onchange('product_id')
    def set_sequence(self):
        order_lines_len = self._context.get('order_line',False)
        if order_lines_len != False:
            for rec in self:
                rec.sequence_no = len(order_lines_len)
                if rec.product_id.accessory_ids:
                    acc = []
                    # for p_acc in rec.product_id.accessory_ids:  
                    #     print("^^^^^^^^^^^^^^^^^^^^",p_acc)
                    #     acc.append({
                    #         'product_id': p_acc.name.id,
                    #         'product_uom_qty':p_acc.accessory_qty,
                    #         'order_id':self.id,
                    #         })
                    #     print("qqqqqqqqqqqqqqqqqqqqqqqqq",acc)
                    #     rec.create({
                    #         'product_id': p_acc.name.id,
                    #         'product_uom_qty':p_acc.accessory_qty,
                    #         'order_id':self.id,
                    #         })
                    #     print("aaaaaaaaaaaaaaaaaaaaaaa",rec)
          