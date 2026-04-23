{
    'name': 'BTS Reminder',
    'version': '17.0.1.0.0',
    'category': 'Services',
    'summary': 'Service reminder system',
    'description': """
        Basic scaffold for BTS Reminder System.
    """,
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/customer_views.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
