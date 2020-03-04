odoo.define('show_order_pos.OrderLists',function(require){
"use strict";

    var gui = require('point_of_sale.gui');
    var core = require('web.core');
    var models = require('point_of_sale.models');
    var pos_screens = require('point_of_sale.screens');
    var QWeb = core.qweb;
    

    models.load_models({

        model: 'pos.order',
        fields: [
            'id', 'name' ,'session_id', 'pos_reference', 
            'partner_id', 'amount_total','lines', 'create_date'],
      
        loaded: function (self, pos_orders) {
            var orders = [];
            for (var i in pos_orders){
                orders[pos_orders[i].id] = pos_orders[i];
            }
            self.pos_orders = orders;
            self.order = [];
            for (var i in pos_orders){
                self.order[i] = pos_orders[i];
            }
        },
    });


    var ListOrders = pos_screens.ActionButtonWidget.extend({
        template: 'ListOrders',

        button_click: function(){

            this.gui.show_screen('OrdersListScreen');
          
        }
    });

    pos_screens.define_action_button({
        'name': 'Show Order',
        'widget': ListOrders,
        'condition': function(){
            return this.pos;
        },
    });


    var OrdersListScreen = pos_screens.ScreenWidget.extend({
        template: 'OrdersListScreen',

        init: function(parent, options){
            this._super(parent, options);
            this.order_string = "";
        },
     
        show: function(){
            var self = this;
            this._super();

            this.renderElement();
            this.$('.back').click(function(){
                self.gui.back();
            });
            var pos_orders = this.pos.pos_orders;
            this.render_list(pos_orders);
          
        },
        

        render_list: function(orders){
            var self = this;
            for(var i = 0, len = Math.min(orders.length,1000); i < len; i++) {
                if (orders[i]) {
                    var order = orders[i];
                    self.order_string += order.pos_reference;
                }
            }
            
            var contents = this.$el[0].querySelector('.orders-lines');
            if (contents){
                contents.innerHTML = "";
                for(var i = 0, len = Math.min(orders.length,1000); i < len; i++) {
                    if (orders[i]) {
                        var order = orders[i];
                        var clientline_html = QWeb.render('OrdersLines', {widget: this, order: order});
                        var orderline = document.createElement('tbody');
                        orderline.innerHTML = clientline_html;
                        orderline = orderline.childNodes[1];
                        contents.appendChild(orderline);
                    }
                }
            }
        },
 
    });

    gui.define_screen({name:'OrdersListScreen', widget: OrdersListScreen});

    return {
        OrdersListScreen: OrdersListScreen
    }
});
