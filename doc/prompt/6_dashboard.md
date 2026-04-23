Create the Odoo 17.0 list view and form view for the daily reminder dashboard in the "bts_reminder" module.

Model: bts.reminder.log (computed daily)
Fields:
- partner_id (Many2one res.partner)
- whatsapp_number (Char, related from partner)
- vehicle_type (Char, related from partner)
- last_service_date (Date, related from partner)
- days_until_due (Integer, computed)
- days_overdue (Integer, computed)
- status (Selection: upcoming/overdue)
- message_draft (Text, computed from active template with placeholders filled)
- send_status (Selection: belum_dikirim/terkirim, default belum_dikirim)

View requirements:
- Tree view grouped by status (upcoming vs overdue)
- Each row shows whatsapp_number and message_draft for easy copying
- Button to mark as "terkirim" per row
- Filter by send_status
- Only accessible by Kepala Bengkel role
- File: views/dashboard_views.xml
- Model file: models/reminder_log.py