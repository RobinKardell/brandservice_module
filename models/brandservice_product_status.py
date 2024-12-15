from odoo import models, fields

class BrandServiceProductStatus(models.Model):
    _name = 'brandservice.product.status'
    _description = 'Brandservice Product Status'

    name = fields.Char(string='Action Name', required=True)
    description = fields.Text(string='Description')