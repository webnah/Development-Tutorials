{
    'name': 'Hospital Management',
    'version': '12.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'Module for managing the Hospitals',
    'sequence': '10',
    'license': 'AGPL-3',
    'author': 'Odoo Mates',
    'maintainer': 'Odoo Mates',
    'website': 'odoomates.com',
    'depends': ['sale'],
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/sequence.xml',
        'data/data.xml',
        'data/cron.xml',
        'wizards/create_appointment.xml',
        'views/patient.xml',
        'views/appointment.xml',
        'views/doctor.xml',
        'reports/patient_card.xml',
        'reports/report.xml',
        'data/mail_template.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
