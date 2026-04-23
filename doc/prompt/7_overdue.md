Create the Odoo 17.0 filtered list view for overdue customers in the "bts_reminder" module.

This is a filtered view of bts.reminder.log where status = 'overdue', showing:
- partner name
- whatsapp_number
- last_service_date
- days_overdue (sorted descending)
- send_status

View requirements:
- Tree view with default filter status = overdue
- Sorted by days_overdue descending
- Color coding: red highlight for days_overdue > 30
- Only accessible by Kepala Bengkel role
- File: append to views/dashboard_views.xml