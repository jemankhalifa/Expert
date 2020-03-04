###################################################################################
# ----------- Backend Customization module -----------
# ----------  Eman Saeed -------------
# *************** Task 6 EXP **************
###################################################################################
{ 
    "name": "Backend Customization",
    "summary":"""Task 6 : EXP""",
    "description": """Backend Customization module is offer these features:
    1- Display database name beside user name in all times like in developer mode.
    2- product accessory where accessories are sub-products while creating sales order accessories 
        should be numbered.
    3- Add workflow to customer page (draft - approved) and make all fields read only when
        state is approved without overriding the view.
    4- Change the colors of the top menu and the side menu.
    5- Add filter by analytic account in accounting general ledger report.""",

    "version": '12.0',   
    "category": 'sale',   
    "author": "Eman Saeed",
    

    "depends": ["product","sale"],
    "data":[
        'security/ir.model.access.csv',
        'views/product_view.xml',
        'views/template_backend_view.xml',
        'views/sale_order_view.xml',
        'views/customer_view.xml'
 
    ],
  
    "sequence": 1,
    "application": False,
    "installable": True,
    "auto_install": False,
}
