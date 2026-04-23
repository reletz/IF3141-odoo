Create the Odoo 17.0 form view and inline action for updating reminder send status in the "bts_reminder" module.

This operates on bts.reminder.log model. Requirements:
- Inline "Tandai Terkirim" button on each row in the dashboard tree view
- When clicked, sets send_status = 'terkirim' and records write_date as sent timestamp
- Confirmation dialog before marking as sent
- Sent records should be visually distinguished (greyed out) in the dashboard
- Only accessible by Kepala Bengkel role
- File: append to views/dashboard_views.xml, add method to models/reminder_log.py