# from odoo import fields,models

# class bankSystemCredit(models.Model):
#     _name="bank.system.services"
#     _description="bank system services"
#     _order = "name"


#     name = fields.Char()
#     account_no=fields.Char()
#     mobile=fields.Char()
#     adhar_card=fields.Char()
#     pan_card=fields.Char()
#     date=fields.Date()
#     address=fields.Char()



from odoo import fields, models

class BankSystemservices(models.Model):
    _name = "bank.system.services"
    _description = "Bank system services"

    customer_name = fields.Char()
    email = fields.Char()
    mobile = fields.Char()
    address = fields.Char()
    pincode = fields.Char()
    adhar_card = fields.Char()
    pan_card = fields.Char()
    occupation = fields.Char()
    father_name = fields.Char()
    date=fields.Date()
    gender=fields.Selection(
        selection=[
            ("male", "Male"),
            ("female", "Female"),
            ("other", "Other"),
        ]
    )



