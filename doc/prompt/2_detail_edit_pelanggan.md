Create the Odoo 17.0 tree view and form view (edit mode) for browsing and updating existing customer data in the "bts_reminder" module.

View requirements:
- Tree view showing: name, whatsapp_number, vehicle_type, license_plate, last_service_date, is_active_customer
- Search bar with filters by: name, license_plate, whatsapp_number, is_active_customer
- Form view (same as customer input form) with embedded One2many list of service history records
- File: views/customer_views.xml (append to existing)