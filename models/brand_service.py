from odoo import models, fields, api
from datetime import datetime

class BrandServiceLine(models.Model):
    _name = 'brand.service.line'
    _description = 'Brand Service Line'

    service_id = fields.Many2one('brand.service', string='Service')
    product_id = fields.Many2one('product.product', string='Product', required=True)
    status = fields.Selection([
        ('new', 'New'),
        ('no_action', 'No Action Required'),
        ('serviced', 'Serviced'),
        ('needs_repair', 'Needs Repair'),
        ('replaced', 'Replaced')
    ], string='Status', default='new')
    notes = fields.Text('Notes')

class BrandService(models.Model):
    _name = 'brand.service'
    _description = 'Brand Service'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'create_date desc'

    name = fields.Char(string='Service Reference', required=True, copy=False, readonly=True, default='New')
    customer_id = fields.Many2one('res.partner', string='Customer', required=True, tracking=True, domain=[('is_company', '=', True)])
    contact_id = fields.Many2one('res.partner', string='Contact Person', tracking=True, domain="[('parent_id', '=', customer_id)]")
    service_date = fields.Date(string='Service Date', default=fields.Date.today, tracking=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft', tracking=True)
    
    service_line_ids = fields.One2many('brand.service.line', 'service_id', string='Service Lines')
    notes = fields.Text(string='Service Notes')
    create_date = fields.Datetime('Created on', readonly=True)
    
    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('brand.service') or 'New'
        return super(BrandService, self).create(vals)

    @api.onchange('customer_id')
    def _onchange_customer_id(self):
        self.contact_id = False