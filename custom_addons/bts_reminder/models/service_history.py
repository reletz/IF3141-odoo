# -*- coding: utf-8 -*-
from odoo import models, fields

class BtsServiceHistory(models.Model):
    _name = 'bts.service.history'
    _description = 'Service History'
    _order = 'service_date desc'

    name = fields.Char(string="Tipe Servis", required=True)
    customer_id = fields.Many2one('res.partner', string="Pelanggan", required=True, ondelete='cascade')
    service_date = fields.Date(string="Tanggal Servis", required=True, default=fields.Date.context_today)
    km_interval = fields.Integer(string="Jarak Tempuh (KM)")
    cost = fields.Float(string="Total Biaya")
