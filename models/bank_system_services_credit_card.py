from odoo import fields,models

class bankSystemCredit(models.Model):
    _name="bank.system.services"
    _description="bank system services"
    _order = "name"


    name = fields.Char()
    account_no=fields.Char()
    mobile=fields.Char()
    adhar_card=fields.Char()
    pan_card=fields.Char()
    date=fields.Date()
    address=fields.Char()