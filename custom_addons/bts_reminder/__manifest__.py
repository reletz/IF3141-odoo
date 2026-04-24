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
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/customer_views.xml',
        'views/service_history_views.xml',
        'views/reminder_parameter_views.xml',
        'views/message_template_views.xml',
        'views/dashboard_views.xml',
        'views/menus.xml',
    ],
    'demo': [
        'data/demo.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
