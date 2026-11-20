"""Task-model extensions for the reminder rules that a plain automation rule can't express."""

# Standard library imports
from collections import defaultdict

# Third party imports
from odoo import api, fields, models


class ProjectTask(models.Model):
  """Adds the daily overdue summary to Odoo's ``project.task``."""

  _inherit = "project.task"

  @api.model
  def _cron_send_overdue_digest(self) -> None:
    """Email each assignee one summary of their open, past-deadline tasks.

    Runs daily, so a task keeps appearing until it is closed. One email per person rather than
    per task, so someone with five overdue tasks gets one message, not five.
    """
    overdue = self.search(
      [
        ("is_closed", "=", False),
        ("is_template", "=", False),
        ("date_deadline", "<", fields.Datetime.now()),
        ("user_ids", "!=", False),
      ]
    )
    tasks_by_user = defaultdict(self.browse)  # browse() with no ids is the empty recordset
    # Pyright sees only Odoo's base classes; fields and methods other add-ons attach at runtime (user_ids
    # from project, send_mail from mail) are invisible to it, hence the two ignores.
    for task in overdue:
      for user in task.user_ids:  # pyright: ignore[reportAttributeAccessIssue]
        tasks_by_user[user] |= task
    template = self.env.ref("company_tasks.mail_template_overdue_digest")
    for user, tasks in tasks_by_user.items():
      template.with_context(overdue_tasks=tasks.sorted("date_deadline")).send_mail(  # pyright: ignore[reportAttributeAccessIssue]
        user.id, email_layout_xmlid="mail.mail_notification_light"
      )
