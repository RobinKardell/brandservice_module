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
    ], string='Action', default='new')
    date = fields.Datetime(string='Date', default=fields.Datetime.now)
    technician_id = fields.Many2one('res.users', string='Technician', default=lambda self: self.env.user)