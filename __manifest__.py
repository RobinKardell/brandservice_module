{
    "name": "Brand Service",
    "version": "1.0",
    "summary": "Manage brand services with customer integration and PDF reporting",
    "description": "Track brand services for customers, manage product statuses, and generate reports in Odoo.",
    "author": "Proreach",
    "license": "LGPL-3",
    "depends": ["base", "mail"],
    "data": [
        'security/ir.model.access.csv',
        "views/brand_service_views.xml",
        "reports/brand_service_report.xml",
        "reports/templates/brand_service_report_template.xml"
    ],
    "installable": True,
    "application": True
}