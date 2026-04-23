# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    whatsapp_number = fields.Char(string="Nomor WhatsApp", required=True)
    vehicle_type = fields.Char(string="Tipe Kendaraan", required=True)
    license_plate = fields.Char(string="Nomor Polisi", required=True)
    vehicle_year = fields.Integer(string="Tahun Kendaraan")
    contact_preference = fields.Selection([
        ('pagi', 'Pagi'),
        ('siang', 'Siang'),
        ('sore', 'Sore')
    ], string="Preferensi Waktu Kontak")
    
    is_active_customer = fields.Boolean(
        string="Pelanggan Aktif", 
        default=True,
        help="Pelanggan aktif akan muncul dalam daftar reminder berkala"
    )
    ring_1 = fields.Boolean(
        string="Wilayah Ring 1",
        help="Centang jika pelanggan berada dalam radius kurang dari 5 km dari bengkel"
    )
    notes = fields.Text(string="Notes (Catatan Internal)")

    last_service_date = fields.Date(string="Tanggal Servis Terakhir", compute="_compute_service_dates", store=True)
    first_service_date = fields.Date(string="Tanggal Servis Pertama", compute="_compute_service_dates", store=True)
    
    service_history_ids = fields.One2many('bts.service.history', 'partner_id', string="Riwayat Servis")

    @api.depends('service_history_ids', 'service_history_ids.service_date')
    def _compute_service_dates(self):
        for record in self:
            histories = record.service_history_ids.sorted(key=lambda h: h.service_date)
            if histories:
                record.first_service_date = histories[0].service_date
                record.last_service_date = histories[-1].service_date
            else:
                record.first_service_date = False
                record.last_service_date = False

    @api.constrains('whatsapp_number', 'license_plate')
    def _check_duplicate_customer(self):
        for record in self:
            if record.whatsapp_number and record.license_plate:
                domain = [
                    ('whatsapp_number', '=', record.whatsapp_number),
                    ('license_plate', '=', record.license_plate),
                    ('id', '!=', record.id)
                ]
                if self.search_count(domain) > 0:
                    raise ValidationError(_("Data pelanggan duplikat! Pelanggan dengan Nomor WhatsApp dan Nomor Polisi yang sama sudah terdaftar di sistem."))
