from odoo import models, fields, api

class BrandServiceReportLine(models.Model):
    _name = 'brandservice.report.line'
    _description = 'Brandservice Report Line'

    report_id = fields.Many2one('brandservice.report', string='Report', ondelete='cascade')
    product_id = fields.Many2one('product.product', string='Product', required=True)
    product_qty = fields.Integer(string='Quantity', default=1)
    line_id = fields.Char(string='Line ID', readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('brandservice.report.line'))
    action_status = fields.Many2one('brandservice.product.status', string='Action', required=True)

class BrandServiceReport(models.Model):
    _name = 'brandservice.report'
    _description = 'Brandservice Report'
    _order = 'date_service desc'

    name = fields.Char(string='Report Name', required=True, default='New')
    customer_id = fields.Many2one('res.partner', string='Customer', required=True, domain=[('is_company', '=', True)])
    contact_person_id = fields.Many2one(
        'res.partner', 
        string='Contact Person', 
        domain="[('parent_id', '=', customer_id)]",
    )
    date_created = fields.Datetime(string='Date Created', default=fields.Datetime.now, readonly=True)
    date_service = fields.Date(string='Service Date', required=True)
    status = fields.Selection([
        ('new', 'New'),
        ('no_action', 'No Action Needed'),
        ('serviced', 'Serviced'),
    ], string='Status', default='new')
    line_ids = fields.One2many('brandservice.report.line', 'report_id', string='Product Lines')