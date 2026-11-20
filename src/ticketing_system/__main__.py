"""Entry point: run Odoo with this project's add-ons, configured from the environment."""

# Standard library imports
import os
import sys
import threading
import time
import urllib.request
from datetime import UTC, datetime
from http import HTTPStatus
from pathlib import Path

# Third party imports
import odoo.cli

ADDONS_DIR = Path(__file__).parent / "addons"
PERSISTED_DIR = Path(os.environ.get("PERSISTED_DIR", "/app/persisted_data"))
HEARTBEAT_FILE = PERSISTED_DIR / "logs" / "heartbeat.txt"
HTTP_PORT = 8069


def _write_heartbeats() -> None:
  """Write the heartbeat file devkit-container's healthcheck reads, while Odoo answers HTTP.

  Probing ``/web/health`` rather than beating unconditionally means a wedged server stops the beats.
  """
  HEARTBEAT_FILE.parent.mkdir(parents=True, exist_ok=True)
  while True:
    try:
      with urllib.request.urlopen(f"http://127.0.0.1:{HTTP_PORT}/web/health", timeout=5) as response:
        healthy = response.status == HTTPStatus.OK
    except OSError:
      healthy = False
    if healthy:
      # Replace atomically so the healthcheck never reads a half-written file.
      tmp = HEARTBEAT_FILE.with_suffix(".tmp")
      tmp.write_text(datetime.now(UTC).isoformat())
      tmp.replace(HEARTBEAT_FILE)
    time.sleep(30)


def run_app() -> None:
  """Start the Odoo server; installs ``company_tasks`` on a fresh database and updates it on every start."""
  db_name = os.environ.get("DB_NAME", "tasks")
  args = [
    "server",
    f"--addons-path={ADDONS_DIR}",
    f"--data-dir={PERSISTED_DIR / 'odoo'}",
    f"--db_host={os.environ.get('DB_HOST', 'ticketing-postgres')}",
    f"--db_port={os.environ.get('DB_PORT', '5432')}",
    f"--db_user={os.environ.get('DB_USER', 'odoo')}",
    f"--db_password={os.environ['DB_PASSWORD']}",
    f"--database={db_name}",
    f"--db-filter=^{db_name}$",
    "--no-database-list",
    "--proxy-mode",
    f"--http-port={HTTP_PORT}",
    # -i creates and initialises the database on the first start; -u applies each release's data
    # (rules, templates) on every later one.
    "--init=company_tasks",
    "--update=company_tasks",
  ]
  if smtp_host := os.environ.get("SMTP_HOST"):
    args += [
      f"--smtp={smtp_host}",
      f"--smtp-port={os.environ.get('SMTP_PORT', '587')}",
      f"--smtp-user={os.environ.get('SMTP_USER', '')}",
      f"--smtp-password={os.environ.get('SMTP_PASSWORD', '')}",
      f"--email-from={os.environ.get('EMAIL_FROM', '')}",
    ]
    if os.environ.get("SMTP_SSL", "").lower() in {"1", "true"}:
      args.append("--smtp-ssl")

  threading.Thread(target=_write_heartbeats, name="heartbeat", daemon=True).start()
  sys.argv = ["odoo", *args]
  odoo.cli.main()


if __name__ == "__main__":
  run_app()
