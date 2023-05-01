from odoo import fields,models

class bankSystemCustomer(models.Model):
    _name="bank.system.customer"
    _description="bank system customer"
    _order = "name"


    name = fields.Char(required=True)
    mobile=fields.Char()
    Select_Banks=fields.Char()
    account_no=fields.Char()
    address=fields.Char()
