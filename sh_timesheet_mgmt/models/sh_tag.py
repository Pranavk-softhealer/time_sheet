# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.
from odoo import fields, models, api


class Sh_tag(models.Model):
    _name = 'sh.tag'
    _description = 'SH TAG'

    name = fields.Char(string='Name', required=True)

