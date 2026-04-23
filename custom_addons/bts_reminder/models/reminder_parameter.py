# -*- coding: utf-8 -*-
from odoo import models, fields

class BtsReminderParameter(models.Model):
    _name = 'bts.reminder.parameter'
    _description = 'Reminder Parameter'
    _rec_name = 'service_type'

    service_type = fields.Selection([
        ('ringan', 'Servis Ringan'),
        ('berat', 'Servis Berat')
    ], string="Jenis Servis", required=True)
    interval_days = fields.Integer(string="Interval Hari", required=True)
    offset_days = fields.Integer(string="Offset (hari sebelum jatuh tempo)", required=True)
    tolerance_days = fields.Integer(string="Toleransi (hari setelah jatuh tempo)", required=True)
    is_active = fields.Boolean(string="Aktif", default=True)
    description = fields.Text(string="Deskripsi Tambahan")
