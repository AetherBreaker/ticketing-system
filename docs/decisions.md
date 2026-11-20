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
4. **The deployment image does not start yet: Odoo refuses `PYTHONOPTIMIZE`**, which devkit-container's Dockerfile
   template sets in every image (after the project windows, so a window cannot override it). Odoo's guard in
   `odoo/init.py` exists because its code relies on 530 `assert` statements (173 files, none in tests) as real
   checks. Options discussed, none chosen:
   - `PYTHONOPTIMIZE=` (empty, i.e. off) in `docker/compose.yaml`;
   - the launcher re-execs itself without it;
   - a devkit-container opt-out (dependency repo: owner's go-ahead and merge);
   - in the fork, rewrite the asserts as `if` guards at build time, keeping `AssertionError` (7 callers catch it).
     Under `-O` that behaves the same as no `-O`; it only satisfies the template.
   - `-OO` additionally strips docstrings: crashes `base_sparse_field` and `odoo upgrade_code`, and blanks the
     model info text, API doc descriptions and CLI help; the memory saved is unmeasured.
5. **Python 3.15 port** (owner interested, for PEP 810 lazy imports; not now). Findings so far: 3.15.0 shipped
   2026-10-09; uv publishes a `python3.15-trixie-slim` image; greenlet, gevent, psycopg2, lxml, pillow and
   cryptography ship cp315 wheels, reportlab builds from its sdist; Odoo's one known break is `UpgradeHook.load_module`
   in `odoo/modules/module.py` (3.15 no longer calls `load_module`); devkit-container's template hard-codes the
   3.14 base image. Lazy imports must keep `odoo.*` eager (models register by import side effect), e.g. through
   `sys.set_lazy_imports_filter` in the launcher. The memory gain is unmeasured.
6. **Project structure**: to be discussed next.
