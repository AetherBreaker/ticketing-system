{  # pyright: ignore[reportUnusedExpression]  -- Odoo reads this file as one dict literal
  "name": "Company Tasks",
  "summary": "Task reminders, overdue nagging and manager escalation on top of Project",
  "version": "20.0.1.0.0",
  "author": "AetherBreaker",
  "license": "LGPL-3",
  "depends": ["project", "hr_timesheet", "base_automation", "mail"],
  "data": [
    "data/settings.xml",
    "data/mail_templates.xml",
    "data/automations.xml",
  ],
  "installable": True,
  "application": False,
}
