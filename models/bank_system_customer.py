from odoo import fields,models

class bankSystemCustomer(models.Model):
    _name="bank.system.customer"
    _description="bank system customer"
    _order = "name"


    name = fields.Char(required=True)
    address=fields.Char()
    mobile=fields.Char()
    Banks=fields.Char()
    account_no=fields.Char()
    adhar_card=fields.Char()
    acc_opened=fields.Date()    