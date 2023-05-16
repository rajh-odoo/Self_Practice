from odoo import fields, models,api
from odoo.exceptions import UserError


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
    state = fields.Selection(
        selection=[
            ("new", "New"),
            ("offer_received", "Offer Received"),
            ("offer_accepted", "Offer Accepted"),
            ("cancel", "Cancel"),
        ],
        string="Status",
        required=True,
        copy=False,
        default="new",
    )
    offer_ids = fields.One2many('bank.system.offers', 'property_id', string="offers")
    amount=fields.Float()
    best_offers = fields.Float(compute="_best_offer", default=0)


    @api.depends("offer_ids.amount")
    def _best_offer(self):
        for record in self:
            record.best_offers = max(
                record.offer_ids.mapped('amount'), default=0)


    @api.ondelete(at_uninstall=False)
    def _deleting_the_offer(self):
        if self.state in ['offer_received', 'offer_accepted']:
            raise UserError("only new and cancel offer can be deleted")            