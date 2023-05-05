from odoo import fields, models

class BankSystemservices(models.Model):
    _name = "bank.system.offers"
    _description = "Bank system offers"

    amount=fields.Float()
    status=fields.Selection(selection=[("accepted","Accepted"),("declined","Declined")],copy=False)
    deadline=fields.date()
    customer_id=fields.Many2one('res.partner')
    
    


   