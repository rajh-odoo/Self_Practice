from odoo import fields, models, api
from odoo.exceptions import UserError


class BankSystemOffer(models.Model):
    _name = "bank.system.offers"
    _description = "Bank system offers"
    
    

    discount = fields.Integer(default=2,readonly=True)
    amount = fields.Float()
    # price=fields.Float()
    status = fields.Selection(selection=[("accepted", "Accepted"), ("refused", "Refused")], copy=False)
    interest_rate = fields.Integer(default=10, readonly=True)
    loan_period = fields.Integer(string="Loan Period (in years)")
    total_amount=fields.Integer(compute='_compute_total_amount')
    property_id=fields.Many2one('bank.system')


    @api.depends('interest_rate','loan_period','amount')
    def _compute_total_amount(self):
        for record in self:
            record['total_amount']=record['amount']+((record['amount']*record['loan_period']*(record['interest_rate']-record['discount']))/100)


    def accepted(self):
        for record in self:
            for record in self.property_id.offer_ids:
                record.status='refused'
            self.status = 'accepted'
            self.property_id.best_offers = record.amount
            self.property_id.state='offer_accepted'        


    def refused(self):
        for record in self:
            record.status='refused'
            self.property_id.state='offer_received'
    

    @api.model
    def create(self, vals):
        temp = self.env['bank.system'].browse(vals['property_id'])
        if temp.best_offers >= vals['amount']:
            raise UserError("amount should be greater than best offer %.2f" %temp.best_offers)    
        return super().create(vals)        
               
    