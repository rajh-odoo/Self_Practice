from odoo import fields, models


class Banking(models.Model):
    _name = "bank.system"
    _description = "Banking system"

    customer_name = fields.Char()
    email = fields.Char()
    mobile = fields.Char()
    address = fields.Char()
    pincode = fields.Char()
    adhar_card = fields.Char()
    pan_card = fields.Char()
    occupation = fields.Char()
    father_name = fields.Char()
    gender=fields.Selection(
        selection=[
            ("male", "Male"),
            ("female", "Female"),
            ("other", "Other"),
        ]
    )