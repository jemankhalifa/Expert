odoo.define('backend_customization.UserMenuTemp', function (require) {
"use strict";

/**
 * This widget is appended by the webclient to the right of the navbar.
 * It displays the avatar and the name of the logged user (and optionally the
 * db name, in debug mode).
 * If clicked, it opens a dropdown allowing the user to perform actions like
 * editing its preferences, accessing the documentation, logging out...
 */

var core = require('web.core');
var framework = require('web.framework');
var Dialog = require('web.Dialog');
var Widget = require('web.Widget');

var _t = core._t;
var QWeb = core.qweb;

var UserMenu = Widget.extend({
    template: 'backend_customization.UserMenuTemp',
    /**
     * @override
     * @returns {Deferred}
     */
    start: function () {
        var self = this;
        var session = this.getSession();
        this.$el.on('click', '[data-menu]', function (ev) {
            ev.preventDefault();
            var menu = $(this).data('menu');
            self['_onMenu' + menu.charAt(0).toUpperCase() + menu.slice(1)]();
        });
        console.log(">>>>>>>>>>>>>>11111111111111111111111");
        return this._super.apply(this, arguments).then(function () {
            var $avatar = self.$('.oe_topbar_avatar');
            if (!session.uid) {
                $avatar.attr('src', $avatar.data('default-src'));
                return $.when();
            }
            var topbar_name = session.name;
           
            topbar_name = _.str.sprintf("%s (%s)", topbar_name, session.db);
            console.log(">>>>>>>>>>>>>>",topbar_name);
            self.$('.oe_topbar_name').text(topbar_name);
            var avatar_src = session.url('/web/image', {
                model:'res.users',
                field: 'image_small',
                id: session.uid,
            });
            $avatar.attr('src', avatar_src);
        });
    },
    });

return UserMenu;

});
