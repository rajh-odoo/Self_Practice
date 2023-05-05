{
    'name': "bank",
    'version': '1.0',
    'depends': ['base'],
    'author': "Ravi Roushan",
    'category': 'Category',
    
    'description': """
    Description text
    """,
    
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/bank_system_views.xml',
        # 'views/bank_system_customer_views.xml',
        'views/bank_system_services_views.xml',
        'views/bank_system_offers_credit_views.xml',
        'views/bank_system_offers_loan_views.xml',
        'views/bank_menus.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
    
       
    ],
    'application':True,
    'installable':True,
    

}