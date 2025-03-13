# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.
from odoo import fields, models, api


class Sh_reason(models.TransientModel):
    _name = 'sh.reason'
    _description = 'rejection reason'

    name = fields.Char(string='Rajection Reason', required=True)

    def reject_reason_button(self):
        current =  self.env.context
        active_model = current.get('active_model')
        active_id = current.get('active_id')
        
        res = self.env[active_model].browse(active_id)
        res.write({"reject_reason":self.name,"state":'reject'})
        # res.reject_reason = self.name
        # res.state = 'reject'

        


       