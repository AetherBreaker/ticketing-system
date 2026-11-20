from collections import defaultdict

from odoo import api, fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    @api.model
    def _cron_send_overdue_digest(self):
        """Email each assignee one summary of their open, past-deadline tasks.

        Runs daily, so a task keeps appearing until it is closed. One email per person rather than
        per task, so someone with five overdue tasks gets one message, not five.
        """
        overdue = self.search([
            ("is_closed", "=", False),
            ("is_template", "=", False),
            ("date_deadline", "<", fields.Datetime.now()),
            ("user_ids", "!=", False),
        ])
        tasks_by_user = defaultdict(lambda: self.browse())
        for task in overdue:
            for user in task.user_ids:
                tasks_by_user[user] |= task
        template = self.env.ref("company_tasks.mail_template_overdue_digest")
        for user, tasks in tasks_by_user.items():
            template.with_context(overdue_tasks=tasks.sorted("date_deadline")).send_mail(
                user.id, email_layout_xmlid="mail.mail_notification_light"
            )
