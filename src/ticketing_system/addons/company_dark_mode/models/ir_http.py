"""Serve the dark asset bundle to browsers that chose it."""

# Third party imports
from odoo import models
from odoo.http import request


class IrHttp(models.AbstractModel):
  """Community ships the dark theme (``web.assets_web_dark``) but its ``color_scheme`` always answers light."""

  _inherit = "ir.http"

  def color_scheme(self) -> str:
    """Return ``"dark"`` when the browser's ``color_scheme`` cookie, set by the user-menu switch, says so."""
    if request and request.cookies.get("color_scheme") == "dark":
      return "dark"
    # Pyright can't see ir.http's methods through Odoo's runtime-built class.
    return super().color_scheme()  # pyright: ignore[reportAttributeAccessIssue]
