Create the Odoo 17.0 form view for inputting new customer data in the "bts_reminder" module.

Model: extend res.partner with additional fields:
- whatsapp_number (Char, required)
- vehicle_type (Char, required)
- license_plate (Char, required)
- vehicle_year (Integer)
- contact_preference (Selection: pagi/siang/sore)
- is_active_customer (Boolean, default True)
- ring_1 (Boolean, label "Wilayah Ring 1")
- notes (Text, optional)
- last_service_date (Date, computed from service history, readonly)
- first_service_date (Date, computed from service history, readonly)

View requirements:
- Form view with grouped fields
- Duplicate prevention based on whatsapp_number and license_plate
- Required field validation on save
- File: views/customer_views.xml
- Model file: models/res_partner_ext.py