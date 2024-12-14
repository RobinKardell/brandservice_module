
{
    "name": "brandservice_module",
    "version": "1.0",
    "summary": "Module for managing brand service tasks and reports",
    "description": "A custom module for managing brand services, connecting them to customers, and generating PDF reports.",
    "author": "Proreach",
    "license": "LGPL-3",
    "depends": ["base", "mail"],
    "data": [
        "views/brand_service_views.xml",
        "reports/brand_service_report.xml",
        "reports/templates/brand_service_report_template.xml"
    ],
    "installable": True,
    "application": True,
    "auto_install": False
}
