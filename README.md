# ticketing-system

Company task tracking on [Odoo Community](https://github.com/odoo/odoo) 20: tasks with assignees, steps
(subtasks) with their own people and deadlines, repeating tasks, time tracking, and automated email
reminders.

## Reminders (`company_tasks` add-on)

| Rule | When | Who |
|---|---|---|
| Due soon | 1 day before a task's deadline | Assignees |
| Daily overdue summary | Every morning at 8:00 Eastern until the task is closed | Each assignee, one email per person |
| Escalation | 2 days after a missed deadline | The project's manager |

Rules, email templates and settings are data files under
[`src/ticketing_system/addons/company_tasks/`](src/ticketing_system/addons/company_tasks/); a deploy applies
them with a module update, overwriting edits made to those records in Odoo's interface.

## Running

- **Deployment:** [`docker/compose.yaml`](docker/compose.yaml), devkit-managed; the image runs
  `run-app-ticketing-system`, which starts Odoo configured from the environment (`DB_*`, `SMTP_*`,
  `EMAIL_FROM`).
- **Local trial:** `docker compose -f compose.trial.yaml up -d`, then install `company_tasks_trial` for
  sample users and tasks and a Mailpit inbox at <http://localhost:8025>. Never install that module in
  production.
