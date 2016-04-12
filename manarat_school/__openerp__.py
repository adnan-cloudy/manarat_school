# -*- coding: utf-8 -*-
{
    'name': "Admission Management",

    'summary': """
        Addmissions""",

    'description': """
        School Addmissions Management
    """,

    'author': "Cloudypedia",
    'website': "http://cloudypedia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Customer Relationship Management',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
	'base',
	'crm'
	],

    # always loaded
    'data': [
		'security/security.xml',
        'security/ir.model.access.csv',
        'templates.xml',
		'views/crm_lead_view.xml',
		'views/res_partner_view.xml',
		'views/crm_case_form_view_oppor.xml',
		'views/crm_case_form_view_oppor_pr_access.xml',
		'crm_lead_menu.xml',
		'data/mail_template_data.xml',
		'data/document_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
	'installable': True,
    'application': True,
    'auto_install': False,
}