Create the Odoo 17.0 dashboard view for customer segmentation insights in the "bts_reminder" module.

View requirements:
- Summary cards showing: total active customers, total overdue, total sent reminders this month
- Tree/list view groupable by: service_type, contact_preference, ring_1, send_status
- Graph view (bar chart) showing visit frequency distribution per customer
- Pivot view for cross-analysis
- Date filter: daily / weekly / monthly
- Only accessible by Kepala Bengkel role
- File: append to views/dashboard_views.xml