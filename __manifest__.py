{
    'name': 'Brandservice Module',
    'version': '1.0',
    'category': 'Services',
    'summary': 'Manage brandservice reports and product actions',
    'depends': ['base', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/brandservice_report_views.xml',
        'views/brandservice_product_status_views.xml',
        'data/ir_sequence_data.xml',
    ],
    'installable': True,
    'application': True,
}