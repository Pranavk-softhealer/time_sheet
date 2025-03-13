# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.
from odoo import fields, models, api


class Sh_task(models.Model):
    _name = 'sh.task'
    _description = 'sh task'

    name = fields.Char(string='Name', required=True)
    amount = fields.Float('Amount')
    timesheet_id = fields.Many2one('sh.timesheet',string='Timesheet')