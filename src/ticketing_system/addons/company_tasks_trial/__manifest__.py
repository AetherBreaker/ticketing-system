{  # pyright: ignore[reportUnusedExpression]  -- Odoo reads this file as one dict literal
  "name": "Company Tasks: local trial data",
  "summary": "Sample users, projects and tasks, and mail sent to the local Mailpit inbox. Never install in production.",
  "version": "20.0.1.0.0",
  "author": "AetherBreaker",
  "license": "LGPL-3",
  "depends": ["company_tasks"],
  "data": [
    "data/mail_server.xml",
    "data/sample_data.xml",
  ],
  "installable": True,
  "application": False,
}
