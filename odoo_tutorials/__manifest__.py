# -*- coding: utf-8 -*-
{
    'name': 'Odoo Mates Tutorials',
    'version': '14.0.1.1.0',
    'summary': 'Odoo Tutorials',
    'sequence': -100,
    'description': """Odoo Tutorials By Odoo Mates""",
    'category': 'Tutorials',
    'author': 'Odoo Bot, Odoo Mates',
    'maintainer': 'Odoo Mates',
    'website': 'https://www.odoomates.tech',
    'license': 'LGPL-3',
    'depends': [
        'website_slides',
    ],
    'data': [
        'data/data.xml',
        'data/slide_data_v12.xml',
        'data/slide_data_v13.xml',
        'data/slide_data_v14.xml',
    ],
    'demo': [],
    'qweb': [],
    'images': ['static/description/banner.gif'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
