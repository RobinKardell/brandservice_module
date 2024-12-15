from odoo import models, fields, api

class BrandService(models.Model):
    _name = 'brand.service'
    _description = 'Brand Service'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Service Reference', required=True, copy=False, readonly=True, default='New')
    date = fields.Date(string='Service Date', default=fields.Date.today)
    customer_id = fields.Many2one('res.partner', string='Customer', required=True, tracking=True)
    product_id = fields.Many2one('product.product', string='Product', required=True, tracking=True)
    location = fields.Char(string='Location')
    serial_number = fields.Char(string='Serial Number')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft', tracking=True)
    notes = fields.Text(string='Service Notes')
    service_type = fields.Selection([
        ('repair', 'Repair'),
        ('maintenance', 'Maintenance'),
        ('inspection', 'Inspection')
    ], string='Service Type', required=True, default='maintenance')
    technician_id = fields.Many2one('res.users', string='Technician', default=lambda self: self.env.user)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('brand.service') or 'New'
        return super(BrandService, self).create(vals)