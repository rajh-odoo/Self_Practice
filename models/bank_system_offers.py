from odoo import fields, models, api


class BankSystemOffer(models.Model):
    _name = "bank.system.offers"
    _description = "Bank system offers"

    discount = fields.Integer(default=2,readonly=True)
    amount = fields.Float()
    status = fields.Selection(selection=[("accepted", "Accepted"), ("refused", "Refused")], copy=False)
    interest_rate = fields.Integer(default=10, readonly=True)
    loan_period = fields.Integer(string="Loan Period (in years)")
    total_amount=fields.Integer(compute='_compute_total_amount')


    @api.depends('interest_rate','loan_period','amount')
    def _compute_total_amount(self):
        self.total_amount=self.amount+((self.amount*self.loan_period*(self.interest_rate-self.discount))/100)

        


    @api.depends('status')
    def accepted_btn(self):
        self.status = "accepted"

    def refused_btn(self):
        self.status = "refused"