Create the Odoo 17.0 model and form view for recording service transaction history in the "bts_reminder" module.

Model: bts.service.history
Fields:
- partner_id (Many2one to res.partner, required)
- service_date (Date, required)
- service_type (Selection: ringan/berat, required)
- vehicle_mileage (Integer)
- complaint (Text)
- action_taken (Text)
- spare_parts (Text)
- total_cost (Float)

View requirements:
- Form view for data entry
- Tree view showing: partner_id, service_date, service_type, vehicle_mileage
- Accessible from inside customer detail form as embedded list (One2many)
- File: views/service_history_views.xml
- Model file: models/service_history.py