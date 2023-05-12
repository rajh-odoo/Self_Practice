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
    property_id=fields.Many2one('bank.system')


    @api.depends('interest_rate','loan_period','amount')
    def _compute_total_amount(self):
        self.total_amount=self.amount+((self.amount*self.loan_period*(self.interest_rate-self.discount))/100)

    @api.depends('status')
    def accepted(self):
        for record in self:
            for record in self.property_id.bank_offer_ids:
                record.status='refused'
            self.status='accepted'


    def refused(self):
        for record in self:
            record.status='refused'
            

    def accepted(self):
        for record in self:
            for record in self.property_id.offer_ids:
                record.status='refused'
            self.status = 'accepted'
            self.property_id.selling_price = record.price
            self.property_id.buyer_id = record.partner_id
            self.property_id.state='offer_accepted'
               



    def refused(self):
            self.status = "refused" 
            self.property_id.state="offer_received"
            self.property_id.selling_price = 0
            self.property_id.buyer_id=""         
            

 