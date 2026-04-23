You are helping me build a custom Odoo 17.0 module called "bts_reminder" for AHASS BTS MOTOR Jatinangor, an authorized Honda motorcycle workshop in Indonesia. The module runs on Odoo 17.0 Community Edition with Python 3.11 and PostgreSQL as the database.

## Architecture
Follow Odoo's MVC pattern strictly:
- Model (M): defined in models/ as Python classes inheriting models.Model
- View (V): defined in views/ as XML files (tree, form, kanban, dashboard)
- Controller (C): handled by Odoo's built-in ORM and action mechanism

The module must be fully modular — each feature is a separate model file and a separate view file. Do not put everything in one file.

## Folder Structure
bts_reminder/
├── __manifest__.py
├── __init__.py
├── models/
│   ├── __init__.py
│   ├── res_partner_ext.py       # customer profile extension
│   ├── service_history.py       # service transaction history
│   ├── reminder_parameter.py    # reminder interval configuration
│   ├── message_template.py      # WhatsApp message templates
│   └── reminder_log.py          # reminder send status log
├── views/
│   ├── menus.xml
│   ├── customer_views.xml
│   ├── service_history_views.xml
│   ├── reminder_parameter_views.xml
│   ├── message_template_views.xml
│   ├── dashboard_views.xml
│   └── access_views.xml
├── security/
│   └── ir.model.access.csv
└── data/
    └── demo.xml

## User Roles
There are three roles with different access levels:
- Frontline / Service Advisor: can input and edit customer data and service history only
- Kepala Bengkel (Workshop Head): full access to all features including configuration, dashboard, reminder log, and user access management

## Business Rules
- The system compares each active customer's last service date against today using configured interval parameters
- Customers are grouped into: "upcoming due" (within offset window) and "overdue" (past tolerance window)
- Message sending is ALWAYS manual — no API calls, no automated sending. The system only generates a personalized draft
- Reminder frequency is maximum once per service cycle per customer
- Customers with opt-out status must never appear in the reminder list

## Conventions
- All model names prefixed with "bts".
- All Python files use UTF-8 encoding header
- Use Odoo field types: Char, Text, Date, Integer, Float, Selection, Many2one, One2many, Boolean
- All user-facing strings in Bahasa Indonesia
- Follow Odoo 17.0 API — do NOT use deprecated APIs from older versions
- Security file must be present before any view can be loaded