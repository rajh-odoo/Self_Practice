from odoo import fields, models


class Banking(models.Model):
    _name = "bank.system"
    _description = "Banking system"

    customer_name = fields.Many2one("res.partner")
    email = fields.Char()
    mobile = fields.Char()
    address = fields.Char()
    pincode = fields.Char()
    adhar_card = fields.Char()
    pan_card = fields.Char()
    occupation = fields.Char()
    father_name = fields.Char()
    application_date=fields.Date()
    bank_offer_ids=fields.One2many("bank.system.offers","property_id")
    gender=fields.Selection(
        selection=[
            ("male", "Male"),
            ("female", "Female"),
            ("other", "Other"),
        ]
    )
    status=fields.Selection(
        selection=[
            ("application","Application"),
            ("process","Process"),
            ("validate","Validate"),
            ("done","Done"),
        ],
        default="application"
    )