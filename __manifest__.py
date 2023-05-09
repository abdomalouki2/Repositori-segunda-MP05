{
    'name': 'Fleet Management',
    'version': '1.0',
    'category': 'Fleet',
    'description': """
        This module manages vehicles and their maintenance.
    """,
    'author': 'Abde-Tarik',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/fleet_vehicle_views.xml'
    ],
    'installable': True,
    'auto_install': True,
}
