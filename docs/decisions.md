# Decisions

Owner decisions are marked **(owner)**; Claude's implementation calls are marked **(Claude)** and stand until the owner
says otherwise.

## Settled

1. **Foundation: Odoo Community 20** (owner, 2026-11-20), over Vikunja, Kanboard, Plane and hosted tools. Chosen for
   its free automation rules (reminders, nagging, escalation), subtasks with their own assignees and deadlines,
   repeating tasks, timesheets, and configuration as code in our own add-on.
2. **Public repository, devkit-managed** (owner, 2026-11-20).
3. **Reachable from the open internet** (owner, 2026-11-20), so releases with security fixes are taken promptly.
4. **Odoo's source becomes our own fork in its own repository** (owner, 2026-11-20), so we can patch Odoo's files and own
   its packaging and pipeline. Planned, not set up yet; see **Planned: Odoo fork** below. Until then the dependency
   is Odoo's dated source release, pinned in `pyproject.toml`.
5. **Trial data lives in its own module, `company_tasks_trial`** (Claude): the Mailpit mail server and sample
   users/tasks must never reach production, where `company_tasks` alone is installed.
6. **The launcher installs `company_tasks` on a fresh database and updates it on every start** (Claude), so a deploy
   applies the release's rules and templates without a manual step.
7. **Heartbeat from the launcher, probing `/web/health`** (Claude), for devkit-container's healthcheck. No `aeth_ext`
   yet (see open item 1).

## Planned: Odoo fork

- A repository holding Odoo's 20.0 branch plus our patches, tracking upstream so its security fixes merge in.
- Its own pipeline builds Odoo's wheel (pure Python, so one wheel serves Linux and Windows) and publishes it to
  SFTPyPI; this project then depends on that version instead of the source tarball, a one-line change here.
- Side benefit: no more building Odoo from source on each machine (minutes on Windows).
- To decide when it is set up: whether devkit manages the fork (Odoo builds with setuptools, not uv), the
  version/tag scheme for our patch releases, and how upstream merges are proposed (e.g. a scheduled workflow
  opening a pull request).

## Open

1. `aeth_ext` in the Odoo process (alerts, central logging, healthchecks.io ping). Both it and Odoo install signal
   handlers, so this needs a look before adopting.
2. White-label scope: owner leaned toward full white label (logo, colors, emails, "Powered by Odoo" footer).
3. Coolify server upgrade: currently 2 GB with heavy swap use; Odoo plus Postgres idle at about 210 MB.
