# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.
from odoo import fields, models, api
from datetime import date

class Sh_timesheet(models.Model):
    _name = 'sh.timesheet'
    _description = 'timesheet'
    _inherit = ['mail.thread.cc',
                # 'mail.thread.blacklist',
                # 'mail.thread.phone',
                'mail.activity.mixin',
                'utm.mixin',
                # 'format.address.mixin',
                'mail.tracking.duration.mixin',
               ]

    name = fields.Char(string='Name', required=True, default='New')
    user_id = fields.Many2one('res.users',string='User',default='self.env.uid')
    description = fields.Html("Description")
    date = fields.Date(string='Date',default=date.today())
    hours = fields.Float(string='Hours')
    tag_ids = fields.Many2many('sh.tag',string='Tags')
    state = fields.Selection([('draft','Draft'),('submitted','Submitted'),('approved','Approved'),('reject','Reject')],default='draft')
    reject_reason = fields.Text('Rejection reason',readonly=True)
    task_ids = fields.One2many('sh.task','timesheet_id',string='Task')
    total_amt = fields.Integer(string='Total Amount',compute="compute_total_amt")
    manager_id = fields.Many2one('res.users',string='Manager')
    saavnakamu = fields.Char(string="SaavNakamu")

    @api.depends('task_ids')
    def compute_total_amt(self):
        for rec in self:
            rec.total_amt = sum([task.amount for task in rec.task_ids])


    def manager_button(self):
        self.state = 'submitted'
    
    def approve_button(self):
        self.state = 'approved'
    
    def smart_clicked(self):
        print('============ smart checking =============')

    @api.model
    def create(self, vals):
        # if vals.get('name', 'New') == 'New':
        vals['name'] = self.env['ir.sequence'].next_by_code('sh.timesheet') or 'New'
        return super(Sh_timesheet, self).create(vals)