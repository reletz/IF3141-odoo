# -*- coding: utf-8 -*-
from odoo import fields, models


class BtsMessageTemplate(models.Model):
    _name = 'bts.message.template'
    _description = 'Template Pesan WhatsApp'
    _rec_name = 'name'

    name = fields.Char(string="Nama Template", required=True)
    service_type = fields.Selection([
        ('ringan', 'Servis Ringan'),
        ('berat', 'Servis Berat'),
        ('all', 'Semua')
    ], string="Jenis Servis", default='all')
    body = fields.Text(string="Isi Template", required=True)
    available_placeholders = fields.Text(
        string="Placeholder yang tersedia: {nama}, {tipe_kendaraan}, {nomor_polisi}, {tanggal_servis_terakhir}, {hari_jatuh_tempo}",
        readonly=True,
        default="{nama}\n{tipe_kendaraan}\n{nomor_polisi}\n{tanggal_servis_terakhir}\n{hari_jatuh_tempo}"
    )
    is_active = fields.Boolean(string="Aktif", default=True)
