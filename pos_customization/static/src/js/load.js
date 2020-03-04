odoo.define('pos_customization.init', function (require) {
    "use strict";

    var models = require('point_of_sale.models');
    var rpc = require('web.rpc');

    models.load_fields('product.product', ['type']);

    models.load_models([{
        loaded: function (self) {
        //console.log("33333333333333333333333333333333333333333");
        // Use RPC to query ids product and get available qty
            var ids = _.keys(self.db.product_by_id).map(function (item) {
                return parseInt(item);
            });

            rpc.query({
                model: 'product.product',
                method: 'read',
                args: [ids, ['qty_available']]
            }).then(function (res) {
                res.forEach(function (product) {
                    self.db.qty_by_product_id[product.id] = product.qty_available;
                });
                self.set_qty();
            });

        
        }
    }],
    );
});