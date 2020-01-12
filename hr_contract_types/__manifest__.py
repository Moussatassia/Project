# -*- coding: utf-8 -*-

{
    'name': 'Les types de contract',
    'version': '13.0.1.1.0',
    'category': 'Generic Modules/Human Resources',
    'summary': """
        Types de contract dans les contracts
    """,
    'description': """Odoo13 Employee Contracts Types,Odoo13 Employee, Employee Contracts, Odoo 13""",
    'author': 'Moussa Solution SA',
    'company': 'Moussa Solution SA Projet',
    'maintainer': 'Moussa Tech Solution',
    'website': 'https://www.moussatassia.com',
    'depends': ['hr','hr_contract'],
    'data': [
        'security/ir.model.access.csv',
        'views/contract_view.xml',
        'data/hr_contract_type_data.xml',
    ],
    'installable': True,
    'images': ['static/description/banner.png'],
    'auto_install': False,
    'application': False,
    'license': 'AGPL-3',
}