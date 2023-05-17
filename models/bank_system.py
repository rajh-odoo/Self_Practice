from odoo import fields, models,api
from odoo.exceptions import UserError


class Banking(models.Model):
    _name = "bank.system"
    _description = "Banking system"

    name=fields.Char()
    customer_name = fields.Many2one("res.partner")
    bank_offer_ids=fields.One2many("bank.system.offers","offer_id")
    email = fields.Char()
    mobile = fields.Char()
    address = fields.Char()
    pincode = fields.Char()
    adhar_card = fields.Char()
    pan_card = fields.Char()
    occupation = fields.Char()
    father_name = fields.Char()
    application_date=fields.Date()
    best_offers = fields.Float(compute="_best_offer", default=0)
    loan_period = fields.Integer(string="Loan Period (in years)")
    offer_ids = fields.One2many('bank.system.offers', 'offer_id', string="offers")
    gender=fields.Selection(
        selection=[
            ("male", "Male"),
            ("female", "Female"),
            ("other", "Other"),
        ]
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


    @api.depends("offer_ids.amount")
    def _best_offer(self):
        for record in self:
            record.best_offers = max(
                record.offer_ids.mapped('amount'), default=0)


    @api.ondelete(at_uninstall=False)
    def _deleting_the_offer(self):
        if self.state in ['offer_received', 'offer_accepted']:
            raise UserError("only new and cancel offer can be deleted")   
            
                     