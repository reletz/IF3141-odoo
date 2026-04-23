Create the Odoo 17.0 model and form view for managing WhatsApp message templates in the "bts_reminder" module.

Model: bts.message.template
Fields:
- name (Char, required)
- service_type (Selection: ringan/berat/all)
- body (Text, required, label "Isi Template")
- available_placeholders (Text, readonly, label "Placeholder yang tersedia: {nama}, {tipe_kendaraan}, {nomor_polisi}, {tanggal_servis_terakhir}, {hari_jatuh_tempo}")
- is_active (Boolean, default True)

View requirements:
- Form view with large text area for template body
- Preview section showing placeholder list
- Tree view listing all templates
- Only accessible by Kepala Bengkel role
- File: views/message_template_views.xml
- Model file: models/message_template.py