odoo.define('pos_customization.product_screen_widget', function (require) {
    "use strict";
    var screens = require('point_of_sale.screens');

    screens.PaymentScreenWidget.include({
        finalize_validation: function () {
            //console.log("Isinde Validation button");
            
            var self = this;
            var order = this.pos.get_order();
            var orderlines = order.get_orderlines();

            if ( self.pos.config.limit_orders === true && (orderlines.length < self.pos.config.min_orders || orderlines.length > self.pos.config.max_orders)){
                    // TODO Eman: instead of alert you must define a popup message
                    alert("You cannot validate this ");      
            }

            this._super();
        }
    });
});