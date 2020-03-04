odoo.define('pos_customization.pos_discount', function (require) {
"use strict";

var core = require('web.core');
var screens = require('point_of_sale.screens');
var PosBaseWidget = require('point_of_sale.BaseWidget');

var _t = core._t;
var OrderWidget = PosBaseWidget.extend({
    template:'OrderWidget',
    
    set_value: function(val) {
    	console.log("+++++++++++++++++++++");
    	var order = this.pos.get_order();
    	if (order.get_selected_orderline()) {
            var mode = this.numpad_state.get('mode');
            if( mode === 'quantity'){
                order.get_selected_orderline().set_quantity(val);
            }else if( mode === 'discount'){
                order.get_selected_orderline().set_discount(val);
            }else if( mode === 'price'){
                var selected_orderline = order.get_selected_orderline();
                selected_orderline.price_manually_set = true;
                selected_orderline.set_unit_price(val);
            }
    	}
    }
})

});
