from odoo import fields, models


class BankSystemOffer(models.Model):
    _name = "bank.system.offers.type"
    _description = "Bank system offers type"
    
    
    name=fields.Char()