Create the Odoo 17.0 model and form view for configuring reminder interval parameters in the "bts_reminder" module.

Model: bts.reminder.parameter
Fields:
- service_type (Selection: ringan/berat, required)
- interval_days (Integer, required, label "Interval Hari")
- offset_days (Integer, required, label "Offset (hari sebelum jatuh tempo)")
- tolerance_days (Integer, required, label "Toleransi (hari setelah jatuh tempo)")
- is_active (Boolean, default True)
- description (Text, optional)

View requirements:
- Form view for creating and editing parameters
- Tree view listing all active parameters
- Only accessible by Kepala Bengkel role
- File: views/reminder_parameter_views.xml
- Model file: models/reminder_parameter.py