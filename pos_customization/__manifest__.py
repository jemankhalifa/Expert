###################################################################################
# ----------- POS Customization module -----------
# ----------  Eman Saeed -------------
# *************** Task 5 EXP **************
###################################################################################
{
    'name': 'POS Customization',
    'version': '12.0',
    'category': 'Point Of Sale',
    'author': 'Eman Saeed',
    
    'summary': 'Task For EXP',
    'description': "Display Stock on hand of products in POS ",
    'depends': ['point_of_sale'],
    'data': [
        'views/assets.xml',
        'views/pos_config_view.xml'
    ],
    
    'qweb': ['static/src/xml/stock_quantity.xml','static/src/xml/all_orders.xml'],
    'installable': True,
    'application': False,
}
