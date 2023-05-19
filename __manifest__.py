{
    'name': "bank",
    'version': '1.0',
    'depends': ['base','mail'],
    'author': "Ravi Roushan",
    'category': 'Category',
    
    'description': """
    Description text
    """,
    
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/bank_system_views.xml',
        'views/bank_system_offers_views.xml',
        'views/bank_system_offers_type_views.xml',
        # 'views/bank_system_customer_views.xml',
        'demo/demo_data.xml',
        'views/bank_menus.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        'demo/demo_data.xml',
    ],
    'application':True,
    'installable':True,
    

}