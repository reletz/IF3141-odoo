# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import api, fields, models


class BtsReminderLog(models.Model):
    _name = 'bts.reminder.log'
    _description = 'Log Reminder Harian'
    _order = 'status asc, days_overdue desc, days_until_due asc, id desc'

    partner_id = fields.Many2one('res.partner', string="Pelanggan", required=True, ondelete='cascade')
    whatsapp_number = fields.Char(string="Nomor WhatsApp", related='partner_id.whatsapp_number', readonly=True)
    vehicle_type = fields.Char(string="Tipe Kendaraan", related='partner_id.vehicle_type', readonly=True)
    last_service_date = fields.Date(string="Tanggal Servis Terakhir", related='partner_id.last_service_date', readonly=True)
    days_until_due = fields.Integer(string="Sisa Hari ke Jatuh Tempo", compute='_compute_reminder_data', store=True)
    days_overdue = fields.Integer(string="Hari Keterlambatan", compute='_compute_reminder_data', store=True)
    status = fields.Selection([
        ('upcoming', 'Upcoming'),
        ('overdue', 'Overdue')
    ], string="Status", compute='_compute_reminder_data', store=True)
    message_draft = fields.Text(string="Draft Pesan", compute='_compute_reminder_data', store=True)
    send_status = fields.Selection([
        ('belum_dikirim', 'Belum Dikirim'),
        ('terkirim', 'Terkirim')
    ], string="Status Kirim", default='belum_dikirim', required=True)
    log_date = fields.Date(string="Tanggal Dashboard", default=fields.Date.context_today, required=True, index=True)

    _sql_constraints = [
        ('uniq_partner_log_date', 'unique(partner_id, log_date)', 'Log reminder pelanggan untuk hari ini sudah ada.')
    ]

    @api.depends('partner_id', 'partner_id.last_service_date')
    def _compute_reminder_data(self):
        today = fields.Date.context_today(self)
        service_history_model = self.env['bts.service.history']
        reminder_param_model = self.env['bts.reminder.parameter']
        template_model = self.env['bts.message.template']

        for record in self:
            record.days_until_due = 0
            record.days_overdue = 0
            record.status = False
            record.message_draft = False

            if not record.partner_id or not record.last_service_date:
                continue

            latest_service = service_history_model.search([
                ('partner_id', '=', record.partner_id.id)
            ], order='service_date desc, id desc', limit=1)
            service_type = latest_service.service_type or 'ringan'

            parameter = reminder_param_model.search([
                ('service_type', '=', service_type),
                ('is_active', '=', True)
            ], limit=1)
            if not parameter:
                continue

            due_date = record.last_service_date + timedelta(days=parameter.interval_days)
            diff_to_due = (due_date - today).days
            diff_overdue = (today - due_date).days

            record.days_until_due = diff_to_due if diff_to_due > 0 else 0
            record.days_overdue = diff_overdue if diff_overdue > 0 else 0

            if 0 <= diff_to_due <= parameter.offset_days:
                record.status = 'upcoming'
            elif diff_overdue > parameter.tolerance_days:
                record.status = 'overdue'
            else:
                continue

            template = template_model.search([
                ('is_active', '=', True),
                ('service_type', '=', service_type)
            ], limit=1)
            if not template:
                template = template_model.search([
                    ('is_active', '=', True),
                    ('service_type', '=', 'all')
                ], limit=1)
            if not template:
                continue

            placeholders = {
                '{nama}': record.partner_id.name or '-',
                '{tipe_kendaraan}': record.partner_id.vehicle_type or '-',
                '{nomor_polisi}': record.partner_id.license_plate or '-',
                '{tanggal_servis_terakhir}': record.last_service_date.strftime('%d-%m-%Y') if record.last_service_date else '-',
                '{hari_jatuh_tempo}': due_date.strftime('%d-%m-%Y'),
            }

            message = template.body or ''
            for key, value in placeholders.items():
                message = message.replace(key, value)
            record.message_draft = message

    def action_mark_terkirim(self):
        self.write({'send_status': 'terkirim'})
        return True

    @api.model
    def action_generate_daily_dashboard(self):
        today = fields.Date.context_today(self)
        partners = self.env['res.partner'].search([
            ('is_active_customer', '=', True),
            ('last_service_date', '!=', False)
        ])

        created_logs = self.browse()
        processed_partner_ids = []
        for partner in partners:
            processed_partner_ids.append(partner.id)
            log = self.search([
                ('partner_id', '=', partner.id),
                ('log_date', '=', today)
            ], limit=1)
            if not log:
                log = self.create({
                    'partner_id': partner.id,
                    'log_date': today,
                })

            if log.status:
                created_logs |= log
            else:
                log.unlink()

        if processed_partner_ids:
            stale_logs = self.search([
                ('log_date', '=', today),
                ('partner_id', 'not in', processed_partner_ids)
            ])
        else:
            stale_logs = self.search([('log_date', '=', today)])
        stale_logs.unlink()

        action = self.env.ref('bts_reminder.action_bts_reminder_dashboard').read()[0]
        action['domain'] = [('id', 'in', created_logs.ids)]
        return action
