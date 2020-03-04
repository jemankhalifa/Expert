odoo.define('pos_stock_realtime.pos', function (require) {
    "use strict";
    var models = require('point_of_sale.models');
    var PosModel = models.PosModel;
    var _super_pos = models.PosModel.prototype;
    var screens = require('point_of_sale.screens');
    var PosDB = require('point_of_sale.DB');

    PosDB.include({
        init: function(options){
            //console.log("inside init to start >>>>>>>>>>>>");
            this._super(options);
            this.qty_by_product_id = {};
        },
    });


    models.PosModel = PosModel.extend({
        set_qty: function () {
            var self = this;
            $('.product-list').find('.stock_quantity').each(function () {
                var $product = $(this).parents('.product');
                var id = parseInt($product.attr('data-product-id'));

                var qty = self.db.qty_by_product_id[id];

                if (qty === false || qty === undefined) {
                    qty = 0;
                }

                $(this).text(qty).show();

            });
        },
       
    });
    screens.ProductListWidget.include({
     
        renderElement: function () {
            console.log("666666666666666666666666");
            this._super();
            var self = this;
            self.pos.set_qty();
               
        }
    });
});