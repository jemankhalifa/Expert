odoo.define('backend_customization.UserMenuTemp', function (require) {
"use strict";

var UserMenuExtend = require('web.UserMenu');

    UserMenuExtend.include({

        start: function () {
            // You can include top menue to show DB name beside user name ( by remove condition if ->debug )
            var self = this;
            var session = self.getSession();
            var topname = _.str.sprintf("%s (%s)", session.name, session.db);
            self.$('.oe_topbar_name').text(topname);

            },
        });
});