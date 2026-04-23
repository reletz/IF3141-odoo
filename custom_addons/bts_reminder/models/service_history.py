# -*- coding: utf-8 -*-
from odoo import models, fields

class BtsServiceHistory(models.Model):
    _name = 'bts.service.history'
    _description = 'Service History'
    _order = 'service_date desc'
    _rec_name = 'service_type'

    partner_id = fields.Many2one('res.partner', string="Pelanggan", required=True, ondelete='cascade')
    service_date = fields.Date(string="Tanggal Servis", required=True, default=fields.Date.context_today)
    service_type = fields.Selection([
        ('ringan', 'Servis Ringan'),
        ('berat', 'Servis Berat')
    ], string="Jenis Servis", required=True)
    vehicle_mileage = fields.Integer(string="Kilometer Kendaraan")
    complaint = fields.Text(string="Keluhan Pelanggan")
    action_taken = fields.Text(string="Tindakan yang Dilakukan")
    spare_parts = fields.Text(string="Spare Parts yang Digunakan")
    total_cost = fields.Float(string="Total Biaya")
