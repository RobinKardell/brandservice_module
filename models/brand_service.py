from odoo import models, fields, api
from datetime import timedelta

class BrandService(models.Model):
    _name = 'brand.service'
    _description = 'Brand Service'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'date desc'

    name = fields.Char(string='Service Name', required=True, tracking=True)
    reference = fields.Char(string='Reference', readonly=True, copy=False)
    customer_id = fields.Many2one('res.partner', string='Customer', required=True, tracking=True)
    product_id = fields.Many2one('product.product', string='Product', required=True, tracking=True)
    location = fields.Char(string='Location')
    action = fields.Selection([
        ('new', 'New'),
        ('service', 'Service'),
        ('replace', 'Replacement'),
        ('none', 'No Action')
    ], string='Action', default='new', tracking=True)
    date = fields.Datetime(string='Date', default=fields.Datetime.now, tracking=True)
    technician_id = fields.Many2one('res.users', string='Technician', default=lambda self: self.env.user)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft', tracking=True)
    notes = fields.Text(string='Notes')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('reference'):
                vals['reference'] = self.env['ir.sequence'].next_by_code('brand.service') or 'New'
        return super().create(vals_list)