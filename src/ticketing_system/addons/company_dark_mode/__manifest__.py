{  # pyright: ignore[reportUnusedExpression]  -- Odoo reads this file as one dict literal
  "name": "Dark Mode",
  "summary": "A Dark mode switch in the user menu, using Community's own dark theme",
  "version": "20.0.1.0.0",
  "author": "AetherBreaker",
  "license": "LGPL-3",
  "depends": ["web"],
  "assets": {
    "web.assets_backend": ["company_dark_mode/static/src/dark_mode_item.js"],
  },
  "installable": True,
  "application": False,
}
